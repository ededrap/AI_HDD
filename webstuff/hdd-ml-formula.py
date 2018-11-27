from webstuff.preprocessor import preprocessor

import csv
import pandas as pd
import numpy as np

def loadCsv(filename):
    lines = csv.reader(open(filename, "r"))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = preprocessor(dataset[i])
    return dataset


def entropy(target_col):
    elements, counts = np.unique(target_col, return_counts=True)
    entropy = np.sum(
        [(-counts[i] / np.sum(counts)) * np.log2(counts[i] / np.sum(counts)) for i in range(len(elements))])
    return entropy

def InfoGain(data, split_attribute_name, target_name="class"):
    total_entropy = entropy(data[target_name])

    vals, counts = np.unique(data[split_attribute_name], return_counts=True)

    Weighted_Entropy = np.sum(
        [(counts[i] / np.sum(counts)) * entropy(data.where(data[split_attribute_name] == vals[i]).dropna()[target_name])
         for i in range(len(vals))])

    Information_Gain = total_entropy - Weighted_Entropy
    return Information_Gain

def ID3(dataset, data, originaldata, features, target_attribute_name="class", parent_node_class=None):
    if len(np.unique(data[target_attribute_name])) <= 1:
        return np.unique(data[target_attribute_name])[0]
    elif len(data) == 0:
        return np.unique(originaldata[target_attribute_name])[
            np.argmax(np.unique(originaldata[target_attribute_name], return_counts=True)[1])]
    elif len(features) == 0:
        return parent_node_class
    else:
        parent_node_class = np.unique(data[target_attribute_name])[
            np.argmax(np.unique(data[target_attribute_name], return_counts=True)[1])]
        item_values = [InfoGain(data, feature, target_attribute_name) for feature in
                       features]
        best_feature_index = np.argmax(item_values)
        best_feature = features[best_feature_index]
        tree = {best_feature: {}}
        features = [i for i in features if i != best_feature]

        for value in np.unique(data[best_feature]):
            value = value
            sub_data = data.where(data[best_feature] == value).dropna()
            subtree = ID3(dataset, sub_data, dataset, features, target_attribute_name, parent_node_class)
            tree[best_feature][value] = subtree

        return (tree)

def predict(query, tree, default=1):
    for key in list(query.keys()):
        if key in list(tree.keys()):
            try:
                result = tree[key][query[key]]
            except:
                return default
            result = tree[key][query[key]]
            if isinstance(result, dict):
                return predict(query, result)
            else:

                return result

def train_test_split(dataset):
    training_data = dataset.iloc[:272].reset_index(drop=True)
    testing_data = dataset.iloc[272:].reset_index(drop=True)

    return training_data, testing_data




def test(data, tree):
    queries = data.iloc[:, :-1].to_dict(orient="records")
    predicted = pd.DataFrame(columns=["predicted"])
    for i in range(len(data)):
        predicted.loc[i, "predicted"] = predict(queries[i], tree, 1.0)
        print(predicted.loc[i,"predicted"])

    print('The prediction accuracy is: ', (np.sum(predicted["predicted"] == data["class"]) / len(data)) * 100, '%')




def main():
    dataset = []
    filename = './data/clevelanddata.csv'
    dataset += loadCsv(filename)
    clusteredfile = open("data/clusteredfile.csv", "w")
    for i in range(len(dataset)):

    for i in range(len(dataset)):
        for j in range(len(dataset[i])):
            if (j == (len(dataset[i]) - 1)):
                clusteredfile.write(str(dataset[i][j]) + "\n")
            else:
                clusteredfile.write(str(dataset[i][j]) + ",")
    clusteredfile.close()
    dataset = pd.read_csv('data/clusteredfile.csv',
                          names=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
                                 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'class', ])
    training_data = train_test_split(dataset)[0]
    testing_data = train_test_split(dataset)[1]
    tree = ID3(dataset, training_data, training_data, training_data.columns[:-1])
    #pprint(tree)
    test(testing_data, tree)

if __name__ == "__main__":
    main()