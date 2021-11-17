# 输入里程、游戏时间和冰淇淋，即可判断约会概率
# 获得norm数据，最大最小值
import norm
dataSet = norm.dataSet
labelSet = norm.labelSet
norm_data, ranges, minVals = norm.norm(dataSet)
# print(norm_data)
# print(ranges)
# print(minVals)
import kNN
import numpy as np
def classifierPerson():
    resultList = ['not at all','in small doses','in large doses']
    miles = float(input("Miles:"))
    games = float(input("Games:"))
    iceCream = float(input("IceCream:"))
    inArr = np.array([miles,games,iceCream])
    classifierResult = kNN.classifier((inArr-minVals)/ranges,norm_data,labelSet,3)
    print("You will probably like this person:",resultList[classifierResult-1])

classifierPerson()