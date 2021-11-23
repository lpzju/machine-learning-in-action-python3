def getNumLeafs(myTree):
    # 首先得到根节点
    # firstNode = myTree.keys()[0]
    # 不能直接对keys进行索引，需先转化成list
    firstNode = list(myTree.keys())[0]
    # print(firstNode)
    # 得到no surfacing
    # 获得根节点对应的字典
    secondDict = myTree[firstNode]
    # 对这个字典进行遍历，如果里面还有字典那就继续遍历
    numLeafs = 0
    for key in secondDict.keys():
        if type(secondDict[key]) == dict:
            numLeafs += getNumLeafs(secondDict[key])
        else:
            # 如果没有了那么叶节点数量 + 1
            numLeafs += 1
    return numLeafs

def getTreeDepth(myTree):
    # 首先得到根节点
    # firstNode = myTree.keys()[0]
    # 不能直接对keys进行索引，需先转化成list
    firstNode = list(myTree.keys())[0]
    # print(firstNode)
    # 得到no surfacing
    # 获得根节点对应的字典
    secondDict = myTree[firstNode]
    # 对这个字典进行遍历，如果里面还有字典那就继续遍历
    # 树的深度要去掉根节点
    maxDepth = 0
    for key in secondDict.keys():
        if type(secondDict[key]) == dict:
            tempDeth = 1 + getTreeDepth(secondDict[key])
        else:
            tempDeth = 1
        if tempDeth > maxDepth:
            maxDepth = tempDeth
    return maxDepth


def retrieveTree(i):
    listOfTrees = [{'no surfacing':{0:'no',1:{'flippers':{0:'no',1:'yes'}}}}, \
                  {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head':{0:'no',1:'yes'}},1:'no'}}}}]
    return listOfTrees[i]

if __name__ == "__main__":
    myTree = retrieveTree(0)
    print(getTreeDepth(myTree))
    print(getNumLeafs(myTree))
    getNumLeafs(myTree)
    # getTreeDepth(myTree)