from pandas import DataFrame
from webstuff.preprocessor import preprocessor
import os.path




import csv
import numpy
import random

BASE = os.path.dirname(os.path.abspath(__file__))
column_headers = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
                  'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']


def entropy(target_col):
    elements, counts = numpy.unique(target_col, return_counts=True)
    entropy = sum(
        [(-counts[i] / sum(counts)) * numpy.log2(counts[i] / sum(counts)) for i in range(len(elements))])
    return entropy


def info_gain(data, split_attribute_name, target_name="class"):
    total_entropy = entropy(data[target_name])

    vals, counts = numpy.unique(data[split_attribute_name], return_counts=True)

    weighted_entropy = sum(
        [(counts[i] / sum(counts)) * entropy(data.where(data[split_attribute_name] == vals[i]).dropna()[target_name])
         for i in range(len(vals))])

    information_gain = total_entropy - weighted_entropy
    return information_gain


def ID3(data, original_data, features, target_attribute_name="class", parent_node_class=None):
    if len(data) == 0:
        return numpy.unique(original_data[target_attribute_name])[
            numpy.argmax(numpy.unique(original_data[target_attribute_name], return_counts=True)[1])]
    elif len(numpy.unique(data[target_attribute_name])) == 1:
        return numpy.unique(data[target_attribute_name])[0]
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


def predict(query, tree, default=1):
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
        predicted.loc[i, "predicted"] = predict(queries[i], tree, 1)
        prediction = predicted.loc[i, "predicted"]

    accuracy = numpy.round(numpy.sum(predicted["predicted"] == data["num"]) / len(data) * 100, 2)
    return prediction, accuracy


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
    print(training_data)
    print(testing_data)

    return training_data, testing_data


def load_csv(filename):
    lines = csv.reader(open(filename, "r"))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = preprocessor(dataset[i])
    return dataset


def gather_data(dataset):
    filename = './data/cleveland_data.csv'
    dataset += load_csv(filename)
    filename = './data/hungarian_data.csv'
    dataset += load_csv(filename)
    filename = './data/switzerland_data.csv'
    dataset += load_csv(filename)
    filename = './data/va_data.csv'
    dataset += load_csv(filename)
    return dataset


def main():
    dataset = gather_data(dataset=[])
    dataset = DataFrame.from_records(dataset, columns=column_headers)
    training_data, testing_data = train_test_split(dataset, 0.85)
    tree = ID3(training_data, dataset, dataset.columns[:-1])
    accuracy = test(testing_data, tree)
    # pprint(tree)
    result = [tree, accuracy]

    #prompt = input().split(",")
    #print(prompt)
    #print(preprocessor(prompt))
    
    return result


def action(inputan, treenya):
    
    inputansplit = inputan.split(",")
    print(inputansplit)
    for i in range (len(inputansplit)) :
        print(inputansplit[i])
        inputansplit[i] = float(inputansplit[i])
    prompt = [inputansplit]

    data = (DataFrame.from_records(prompt, columns=column_headers[:-1])).iloc[:, :].to_dict(orient="records")
    #prediction, accuracy = test(testing_data, tree)
    # return tree
    print(prediction)
    print(accuracy)


    prediction  = predict(data[0], treenya, 1)
    

    #test(DataFrame.from_records(prompt, columns=column_headers), tree)
    
    return prediction


if __name__ == "__main__":
    main()
