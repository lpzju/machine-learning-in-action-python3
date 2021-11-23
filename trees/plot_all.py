import getNodesNum as gnn
import matplotlib.pyplot as plt

# 这一段之前画图已解释过
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")

# 这里传入四个参数，如果去除对齐之类的，可以不要xycoords='axes fraction'、textcoords='axes fraction'、va="center", ha="center"
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction',
                            xytext=centerPt, textcoords='axes fraction',
                            va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)


# matplotlib.pyplot.text(x,y,s,fontdict=None,withdash=False,**kwargs)
# 这里是和annotate很像，主要传入坐标位置和要写的东西
def plotMidText(centerPt, parentPt, txtString):
    # 获取父节点与子节点的中间位置，然后写上数据
    # 这里先减再加而不是直接分别去一半，可以避免溢出，但是也没必要
    xMid = (parentPt[0] - centerPt[0]) / 2.0 + centerPt[0]
    yMid = (parentPt[1] - centerPt[1]) / 2.0 + centerPt[1]
    createPlot.ax1.text(xMid, yMid, txtString)


def plotTree(myTree, parentPt, nodeTxt):
    numLeafs = gnn.getNumLeafs(myTree)
    # 获得叶子数目,这里我用的书上第二个例子，叶子数首先是4，第二次变成2
    print("numLeafs:",numLeafs)
    # 这里没用到深度，但是深度第一次是2，第二次是1
    depth = gnn.getTreeDepth(myTree)
    print("depth",depth)
    firstStr = list(myTree.keys())[0]
    print("firstStr:",firstStr)
    print("xOff:", plotTree.xOff)
    print("plotTree.yOff:",plotTree.yOff)
    centerPt = (plotTree.xOff + (1 + numLeafs) / 2 / plotTree.totalW, plotTree.yOff)
    print("totalW:",plotTree.totalW)
    print("totalD:", plotTree.totalD)
    print("centerPtPt:", centerPt)
    print("parentPt:",parentPt)
    plotMidText(centerPt, parentPt, nodeTxt)
    # 从上面的输出来看，第一次的centerPt和parentPt是同一个位置，第一次调用plotMidText、plotNode没有输出内容
    plotNode(firstStr, centerPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    # 下一层的y位置
    plotTree.yOff = plotTree.yOff - 1 / plotTree.totalD
    print("plotTree.yOff:",plotTree.yOff)
    print("--------------------")
    for key in secondDict.keys():
        if type(secondDict[key]) == dict:
            plotTree(secondDict[key], centerPt, str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1 / plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), centerPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), centerPt, str(key))
    # 注意这里还要再把yOff恢复到原来水平
    plotTree.yOff = plotTree.yOff + 1 / plotTree.totalD



def createPlot(inTree):
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    # axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon=False) #, **axprops
    plotTree.totalD = float(gnn.getTreeDepth(inTree))
    plotTree.totalW = float(gnn.getNumLeafs(inTree))
    plotTree.xOff = -0.5 / plotTree.totalW
    plotTree.yOff = 1.0
    plotTree(inTree, (0.5, 1.0), '')
    plt.show()


if __name__ == "__main__":
    myTree = {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}},3:'maybe'}}
    createPlot(myTree)
