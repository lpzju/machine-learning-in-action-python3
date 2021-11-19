import shannonEnt

dataSet = shannonEnt.dataSet
labelSet = shannonEnt.labelSet


def splitDataSet(dataSet, axis, value):
    featureDataSet = []
    for featureVec in dataSet:
        if featureVec[axis] == value:
            tempVec = featureVec[:axis]
            tempVec.extend(featureVec[axis + 1:])
            featureDataSet.append(tempVec)
    return featureDataSet


# a = splitDataSet(dataSet, 0, 0)
# b = splitDataSet(dataSet, 0, 1)
# print(a)
# print(b)


def bestFeature(dataSet):
    # 获得特征(属性)个数，这里为2
    featureNum = len(dataSet[0]) - 1
    # 按西瓜书来看，计算Ent(D)
    totalEntropy = shannonEnt.calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(featureNum):
        # 匿名函数，[1, 1, 1, 0, 0]，[1, 1, 0, 1, 1]
        # 即获得每个属性对应的列向量
        featList = [example[i] for example in dataSet]
        # print(featList)
        # 知道每个属性可能有的取值
        uniqueVals = set(featList)
        # print(uniqueVals)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,i,value)
            prob = len(subDataSet)/len(dataSet)
            newEntropy += prob*shannonEnt.calcShannonEnt(subDataSet)
        infoGain = totalEntropy - newEntropy
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i

    return bestFeature

if __name__ == "__main__":
    result = bestFeature(dataSet)
    print(result)