# 打算重头好好再写写这个
from math import log

# 数据集
dataSet = [[1, 1, 'yes'],
           [1, 1, 'yes'],
           [1, 0, 'no'],
           [0, 1, 'no'],
           [0, 1, 'no']]
# 属性
labelSet = ['no surfacing', 'flippers']


# 首先明确一下任务，最终要做的事情是进行决策树分类任务
# 划分一下小任务，有计算信息熵和划分子集再进行信息增益，还有当标记一致时要选个最多的
# 以及比较重要的属性选择，和决策树迭代构建

# 这里传入一个数据集，然后输出信息熵
def calcShannonEnt(dataSet):
    dict1 = {}
    # 从数据集中要对最后一列的 'yes','yes','no','no','no' 这5个分类进行计算
    for data in dataSet:
        label = data[-1]
        if label not in dict1:
            # 若不在则进行初始化
            dict1[label] = 0
        dict1[label] += 1
    # 然后进行计算
    # 先初始化一个entropy
    data_entropy = 0
    for key in dict1:
        # 这里如果不是.items()，默认就是.keys()
        prop = dict1[key] / len(dataSet)
        data_entropy -= prop * log(prop, 2)
    return data_entropy


# 这时候先验证一下这个函数的正确性
# print(calcShannonEnt(dataSet))
# 0.9709505944546686

# 然后对指定的数据集，列和具体值，返回分割出来的子集
def splitDataSet(dataSet, axis, value):
    # 子集先初始化为空
    subDataSet = []
    for data in dataSet:
        # 对data的每一行，如果指定axis的值是value，那么除了此列的值存储到子列中
        if data[axis] == value:
            tempList = data[:axis]
            tempList.extend(data[axis + 1:])
            subDataSet.append(tempList)
    return subDataSet


# 验证一下
# print(splitDataSet(dataSet,0,1))
# [[1, 'yes'], [1, 'yes'], [0, 'no']]

# 属性选择，输入时数据集，输出是列的值，注意这里是列的值，想要具体的label，还要到labelSet去找
def bestFeature(dataSet):
    # 想要得到最优属性，这里我们使用ID3算法，那么需要计算信息熵和信息增益
    totalEnt = calcShannonEnt(dataSet)
    # 这里先写，写到后面想起要加best_Gain和best_feature
    best_Gain = 0
    best_feature = -1
    # 这里要知道数据集有几个属性，然后从属性中进行遍历
    dataDim = len(dataSet[0]) - 1
    for column in range(dataDim):
        # 获得每一列的数据
        featureList = [example[column] for example in dataSet]
        # 获得每一列数据的取值情况
        uniqueList = set(featureList)
        valGain = 0
        for val in uniqueList:
            # 获得子集，然后再去算Gain
            subSet = splitDataSet(dataSet, column, val)
            prop = len(subSet) / len(dataSet)
            valGain += prop * calcShannonEnt(subSet)
        temp_Gain = totalEnt - valGain
        if temp_Gain > best_Gain:
            best_Gain = temp_Gain
            best_feature = column
    return best_feature


# 0
# print(bestFeature(dataSet))

# 再来定义一下，当标记需要取最多时的函数
# 输入一个列表，输出其中最多的标记
def majorityCnt(classList):
    tempDict = {}
    # 遍历，先把classList中的值存进字典中
    for label in classList:
        if label not in tempDict:
            tempDict[label] = 0
        tempDict[label] += 1
    # 然后进行排序
    sorted_list = sorted(tempDict.items(), key=lambda x: x[1], reverse=True)
    return sorted_list[0][0]

# print(majorityCnt(['a','b','c','b']))
# b


# 最后，进行种树
# 传入的参数是dataSet和labelSet，输出的是一棵树
def createTree(dataSet, labelSet):
    # 首先得到标记
    classList = [example[-1] for example in dataSet]
    # 不放心的话可以先输出一下
    # ['yes', 'yes', 'no', 'no', 'no']
    # print(classList)
    # 这里先进行两个判断(不清楚的话可以再看一下西瓜书的图4.2)
    # 如果classList中全是yes，那么直接输出yes，反之为no也一样
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    # 如果没有属性了，那么输出标记最多的，后面迭代的时候数据集和标记也会更换
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    # 选择最优列
    bestFeat = bestFeature(dataSet)
    # 得到最优列对应的label，这里一开始为no surfacing
    bestLabel = labelSet[bestFeat]
    # 开始栽树
    myTree = {bestLabel: {}}
    # 这时候no surfacing已经没用了，我们把它删掉，做成subLabelSet
    del (labelSet[bestFeat])
    # 现在我们要对刚刚选出来的列进行迭代种树
    # 比如第一次选择的第1列，其中第1列的值为[1,1,1,0,0]，我们应该对其中的0和1分别进行种树
    valSet = [example[bestFeat] for example in dataSet]
    # 然后得到0和1
    uniqueVal = set(valSet)
    for value in uniqueVal:
        subDataSet = splitDataSet(dataSet, bestFeat, value)
        subLabelSet = labelSet[:]
        # 前面已经完成了第1个key，并且我们放置的是bestLabel也就是no surfacing
        # 现在我们对其value进行赋值
        myTree[bestLabel][value] = createTree(subDataSet, subLabelSet)
    return myTree

if __name__ == "__main__":
    result = createTree(dataSet, labelSet)
    print(result)
    # {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
