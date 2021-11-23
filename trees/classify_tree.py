def classify(inputTree,featLabels,testVec):
    firstStr = list(inputTree.keys())[0]
    print("firstStr:",firstStr)
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    print("featIndex:",featIndex)
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]) == dict:
                classLabel = classify(secondDict[key],featLabels,testVec)
            else:
                classLabel = secondDict[key]
    return classLabel


if __name__ == "__main__":
    labels = ['no surfacing','flippers']
    myTree = {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}},3:'maybe'}}
    result = classify(myTree,labels,[1,0])
    print(result)