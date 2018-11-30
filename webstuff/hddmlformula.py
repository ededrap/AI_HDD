from pandas import DataFrame

import numpy
import random

column_headers = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
                  'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']


def entropy(target_col):
    elements, counts = numpy.unique(target_col, return_counts=True)
    entropy = sum(
        [(-counts[i] / sum(counts)) * numpy.log2(counts[i] / sum(counts)) for i in range(len(elements))])
    return entropy


def info_gain(data, split_attribute_name, target_name="num"):
    total_entropy = entropy(data[target_name])

    vals, counts = numpy.unique(data[split_attribute_name], return_counts=True)

    weighted_entropy = sum(
        [(counts[i] / sum(counts)) * entropy(data.where(data[split_attribute_name] == vals[i]).dropna()[target_name])
         for i in range(len(vals))])

    information_gain = total_entropy - weighted_entropy
    return information_gain


def ID3(data, original_data, features, target_attribute_name="num", parent_node_class=None):
    if len(numpy.unique(data[target_attribute_name])) <= 1:
        return numpy.unique(data[target_attribute_name])[0]
    elif len(data) == 0:
        return numpy.unique(original_data[target_attribute_name])[
            numpy.argmax(numpy.unique(original_data[target_attribute_name], return_counts=True)[1])]
    elif len(features) == 0:
        return parent_node_class
    else:
        parent_node_class = numpy.unique(data[target_attribute_name])[
            numpy.argmax(numpy.unique(data[target_attribute_name], return_counts=True)[1])]
        item_values = [info_gain(data, feature, target_attribute_name) for feature in features]
        best_feature_index = numpy.argmax(item_values)
        best_feature = features[best_feature_index]
        tree = {best_feature: {}}
        features = [i for i in features if i != best_feature]

        for value in numpy.unique(data[best_feature]):
            sub_data = data.where(data[best_feature] == value).dropna()
            subtree = ID3(sub_data, original_data, features, target_attribute_name, parent_node_class)
            tree[best_feature][value] = subtree

        return tree


def predict(query, tree, default=1.0):
    for key in query.keys():
        if key in tree.keys():
            try:
                result = tree[key][query[key]]
                if isinstance(result, dict):
                    return predict(query, result)
                else:
                    return result
            except KeyError:
                return default


def test(data, tree):
    queries = data.iloc[:, :-1].to_dict(orient="records")
    predicted = DataFrame(columns=["predicted"])
    for i in range(len(data)):
        predicted.loc[i, "predicted"] = predict(queries[i], tree, 1.0)

    accuracy = numpy.round(numpy.sum(predicted["predicted"] == data["num"]) / len(data) * 100, 2)

    true_positive = list(predicted.where(predicted["predicted"] == data["num"]).dropna()["predicted"]).count(1.0)
    false_positive = list(predicted.where(predicted["predicted"] != data["num"]).dropna()["predicted"]).count(1.0)
    false_negative = list(predicted.where(predicted["predicted"] != data["num"]).dropna()["predicted"]).count(0.0)

    precision = numpy.round(true_positive / (true_positive + false_positive) * 100, 2)
    recall = numpy.round(true_positive / (true_positive + false_negative) * 100, 2)

    return accuracy, precision, recall


def train_test_split(dataset, split_ratio):
    train_size = int(len(dataset.index) * split_ratio)
    training_data = DataFrame(columns=column_headers)
    testing_data = DataFrame(columns=column_headers)
    for x in range(train_size):
        i = random.randrange(len(dataset.index))
        training_data = training_data.append(dataset.iloc[i], ignore_index=True)

    for x in range(len(dataset.index) - train_size):
        i = random.randrange(len(dataset.index))
        testing_data = testing_data.append(dataset.iloc[i], ignore_index=True)
    return training_data, testing_data


def train(dataset):
    dataset = DataFrame.from_records(dataset, columns=column_headers)
    training_data, testing_data = train_test_split(dataset, 0.65)
    tree = ID3(training_data, dataset, dataset.columns[:-1])
    accuracy, precision, recall = test(testing_data, tree)

    return tree, accuracy, precision, recall


def ask(query, tree):
    query_split = query.split(",")
    for i in range(len(query_split)):
        query_split[i] = float(query_split[i])
    prompt = [query_split]

    data = DataFrame.from_records(prompt, columns=column_headers[:-1]).iloc[:, :].to_dict(orient="records")

    prediction = predict(data[0], tree, 1.0)
    
    return prediction


# if __name__ == "__main__":
#     result = train(gather_data())
#     print(result[0])
#     print(result[1])
#     print(result[2])
#     print(result[3])
