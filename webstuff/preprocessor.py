import csv
import os.path

BASE = os.path.dirname(os.path.abspath(__file__))


def load_csv(filename):
    lines = csv.reader(open(os.path.join(BASE, filename), "r"))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = preprocessor(dataset[i])
    return dataset


def gather_data():
    dataset = []
    filename = './data/cleveland_data.csv'
    dataset += load_csv(filename)
    filename = './data/hungarian_data.csv'
    dataset += load_csv(filename)
    filename = './data/switzerland_data.csv'
    dataset += load_csv(filename)
    filename = './data/va_data.csv'
    dataset += load_csv(filename)
    return dataset


def preprocessor(data):
    for i in range(len(data)):
        if data[i] == '?':
            data[i] = '-9.0'
        if i == 0:
            data[i] = age_category(float(data[i]))
        elif i == 3:
            data[i] = bps_category(float(data[i]))
        elif i == 4:
            data[i] = chol_category(float(data[i]))
        # elif i == 7:
        #    data[i] = thalach(float(data[i]))
        elif i == 7:
            data[i] = heart_rate_category(float(data[i]))
        # elif i == 9:
        #    data[i] = oldpeak(float(data[i]))
        elif i == 13:
            if data[i] != "0":
                data[i] = 1
        data[i] = float(data[i])

    return data


def age_category(age):
    if age < 20:
        return 0
    elif age < 30:
        return 1
    elif age < 40:
        return 2
    elif age < 50:
        return 3
    elif age < 60:
        return 4
    elif age < 70:
        return 5
    else:
        return 6


def bps_category(bps):
    if bps < 120:
        return 0
    elif bps < 130:
        return 1
    elif bps < 140:
        return 2
    elif bps < 180:
        return 3
    else:
        return 4


def chol_category(chol):
    if chol < 200:
        return 0
    elif chol < 230:
        return 1
    elif chol < 260:
        return 2
    elif chol < 290:
        return 3
    elif chol < 320:
        return 4
    else:
        return 5


def heart_rate_category(rate):
    if rate < 150:
        return 0
    elif rate < 160:
        return 1
    elif rate < 170:
        return 2
    elif rate < 180:
        return 3
    elif rate < 190:
        return 4
    elif rate < 200:
        return 5
    else:
        return 6


def thalach(rate):
    if rate < 80:
        return 0
    elif rate < 100:
        return 1
    elif rate < 120:
        return 2
    elif rate < 140:
        return 3
    elif rate < 160:
        return 4
    elif rate < 180:
        return 5
    elif rate < 200:
        return 6
    else:
        return 7
