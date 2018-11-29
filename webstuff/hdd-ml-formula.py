from pandas import DataFrame
from webstuff.preprocessor import preprocessor

import csv
import numpy as np

column_headers = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
                  'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']


def entropy(target_col):
    elements, counts = np.unique(target_col, return_counts=True)
    entropy = sum(
        [(-counts[i] / sum(counts)) * np.log2(counts[i] / sum(counts)) for i in range(len(elements))])
    return entropy


def info_gain(data, split_attribute_name, target_name="num"):
    total_entropy = entropy(data[target_name])

    vals, counts = np.unique(data[split_attribute_name], return_counts=True)

    weighted_entropy = sum(
        [(counts[i] / sum(counts)) * entropy(data.where(data[split_attribute_name] == vals[i]).dropna()[target_name])
         for i in range(len(vals))])

    information_gain = total_entropy - weighted_entropy
    return information_gain


def ID3(data, original_data, features, target_attribute_name="num", parent_node_class=None):
    if len(data) == 0:
        return np.unique(original_data[target_attribute_name])[
            np.argmax(np.unique(original_data[target_attribute_name], return_counts=True)[1])]
    elif len(np.unique(data[target_attribute_name])) == 1:
        return np.unique(data[target_attribute_name])[0]
    elif len(features) == 0:
        return parent_node_class
    else:
        parent_node_class = np.unique(data[target_attribute_name])[
            np.argmax(np.unique(data[target_attribute_name], return_counts=True)[1])]
        item_values = [info_gain(data, feature, target_attribute_name) for feature in features]
        print(item_values)
        best_feature_index = np.argmax(item_values)
        print(best_feature_index)
        best_feature = features[best_feature_index]
        print(best_feature)
        tree = {best_feature: {}}
        features = [i for i in features if i != best_feature]

        for value in np.unique(data[best_feature]):
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
        prediction = (predicted.loc[i, "predicted"])

    accuracy = 'The prediction accuracy is: ', (np.sum(predicted["predicted"] == data["num"]) / len(data)) * 100, '%'
    return prediction, accuracy


def train_test_split(dataset, split_ratio):
    train_size = int(len(dataset.index) * split_ratio)
    training_data = dataset.iloc[:train_size].reset_index()
    testing_data = dataset.iloc[train_size:].reset_index()

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
    training_data, testing_data = train_test_split(dataset, 0.95)
    tree = ID3(training_data, dataset, dataset.columns[:-1])
    prediction, accuracy = test(testing_data, tree)
    # return tree
    print(prediction)
    print(accuracy)

    # prompt = [input().split(",")]
    # print(prompt)
    # test(DataFrame.from_records(prompt, columns=column_headers), tree)


if __name__ == "__main__":
    main()
