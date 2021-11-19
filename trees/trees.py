import majority
import featureSelect

dataSet = featureSelect.dataSet
labelSet = featureSelect.labelSet


def createTree(dataSet, labelSet):
    # classList = ['yes','yes','no','no','no']
    # 这是要分类情况
    classList = [example[-1] for example in dataSet]
    # 如果此时属性都已划分完，则返回最多的类
    if classList.count(classList[0]) == len(classList):
        return classList[0]  # 第一轮次yes为2，no为3，所以继续
    if len(dataSet[0]) == 1:
        # 若只有yes或者no这样的标记，那么需要选择类最多的
        return majority.majorityCnt(classList)
    # 接下来需要选择最有属性bestFeat
    bestFeat = featureSelect.bestFeature(dataSet)
    # 第一次选择的最优属性为0，这个0是列的意思
    # 我们从labelSet=['no surfacing','flippers']选no surfacing
    bestFeatLabel = labelSet[bestFeat]
    # 开始栽树
    # 一开始是{no surfacing:{}}，参照P43页最上方

    myTree = {bestFeatLabel: {}}
    # 删掉no surfacing
    del (labelSet[bestFeat])
    # 按照属性选择的那一套，开始选择属性
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    # 对于uniqueVals得到的0和1，按照属性选择里面的，划分子集
    for value in uniqueVals:
        subLabels = labelSet[:]
        # 迭代栽树
        subData = featureSelect.splitDataSet(dataSet,bestFeat,value)
        # 既然是迭代，那就传入新的data和新的label，这样更清晰一点
        myTree[bestFeatLabel][value] = createTree(subData, subLabels)
    return myTree


if __name__ == "__main__":
    result = createTree(dataSet, labelSet)
    print(result)
