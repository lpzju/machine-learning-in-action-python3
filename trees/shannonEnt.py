from math import log

dataSet = [[1, 1, 'yes'],
           [1, 1, 'yes'],
           [1, 0, 'no'],
           [0, 1, 'no'],
           [0, 1, 'no']]

labelSet = ['no surfacing', 'flippers']


def calcShannonEnt(dataSet):
    dataNum = len(dataSet)
    dict1 = {}
    for data in dataSet:
        label = data[-1]
        if label not in dict1:
            dict1[label] = 0
        dict1[label] += 1
    shannonEnt = 0
    for key in dict1:
        prob = dict1[key] / dataNum
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


if __name__ == "__main__":
    result = calcShannonEnt(dataSet)
    print(result)
