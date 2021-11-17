import numpy as np
import kNN


def txt2vec(filename):
    # 32*32的规模，用1*1024的向量接收
    vecContent = np.zeros((1, 1024))
    with open(filename, 'r') as fobj:
        for i in range(32):
            line = fobj.readline()
            for j in range(32):
                vecContent[0, 32 * i + j] = int(line[j])
        return vecContent


# 打印输出看一下结果
# filename = './trainingDigits/0_0.txt'
# a = txt2vec(filename)
# print(a[0, 0:64])

trainingFilePath = './trainingDigits'
testFilePath = './testDigits'

from os import listdir


def hwPredict():
    # 获得trainingDigits的各文件
    trainingFileList = listdir(trainingFilePath)
    # 获得标记集
    labelSet = []
    dataSetNum = len(trainingFileList)
    # 获得数据集
    dataSet = np.zeros((dataSetNum, 1024))
    # print(dataSetNum)
    for i in range(dataSetNum):
        # 获得每一个txt文件
        eachTrainingFile = trainingFileList[i]
        # 因为文件时0_0.txt类型，所以先按.分割，再按_分割
        eachTrainingFile = eachTrainingFile.split('.')[0]
        eachTrainingFileLabel = int(eachTrainingFile.split('_')[0])
        labelSet.append(eachTrainingFileLabel)
        # 通过txt2vec获得数据集
        trainingFilename = 'trainingDigits/' + eachTrainingFile + '.txt'
        dataSet[i, :] = txt2vec(trainingFilename)
        # print(len(dataSet))
        # print(dataSet.shape)
        # print(type(dataSet))
        # print(labelSet)
    # 现在我们的数据集和label都做好了
    # 开始用测试集的数据来进行判断

    testFileList = listdir(testFilePath)
    # print(testFileList)
    errorCount = 0.0
    testSetNum = len(testFileList)
    # print(testSetNum)
    for i in range(testSetNum):
        # 老样子，先进行每个向量的划分
        eachTestFile = testFileList[i]
        # print(eachTestFile)
        eachTestFile = eachTestFile.split('.')[0]
        # print(eachTestFile)
        eachTestFileLabel = int(eachTestFile.split('_')[0])
        # 转换成向量
        testFilename = 'trainingDigits/' + eachTestFile + '.txt'
        testVector = txt2vec(testFilename)
        # print(testVector)
        testClassifierResult = kNN.classifier(testVector,dataSet,labelSet,3)
        print("the classifier came back with:%d,the real answer is:%d"%(testClassifierResult,eachTestFileLabel))
        if testClassifierResult != eachTestFileLabel:
            errorCount += 1.0
    print("\nthe total number of errors is:",errorCount)
    print("\nthe total error rate is:",errorCount/testSetNum)

hwPredict()
