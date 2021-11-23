# 再次重写一下决策树
# 搞清楚逻辑

# 几个功能去实现：
# 1.画指向，也就是之前的annotate
# 2.画线条上的内容，也就是text，这里需要centerPt和parentPt坐标，然后取一半
# 3.创建画布，然后给出根节点，然后开始画树
# 4.画树

import matplotlib.pyplot as plt
import getNodesNum as gnn

# 定义父节点和叶子节点的样式
leafNode = dict(boxstyle="sawtooth",fc="0.8")
decisionNode = dict(boxstyle="round4",fc="0.8")
arrow_args = dict(arrowstyle="<-")

# 画指向
def plotNode(nodeTxt,parentPt,centerPt,nodeType):
    # va在书上的作用是保持对齐，可以不加看看效果
    createPlot.ax1.annotate(nodeTxt,xy=parentPt,xytext=centerPt,bbox=nodeType,arrowprops=arrow_args)

# 画线上的内容
def plotMidContent(nodeTxt,parentPt,centerPt):
    xMid = (parentPt[0]+centerPt[0])/2
    yMid = (parentPt[1]+centerPt[1])/2
    createPlot.ax1.text(xMid,yMid,nodeTxt)

def plotTree(myTree,parentPt,nodeTxt):
    numLeafs = gnn.getNumLeafs(myTree)
    # 对传入进来的‘树’，首先画根结点，然后判断它下面是否还有字典，有就递归
    # 要对根节点进行绘画的话，我们需看一下plotMidContent和plotTree需要传入的参数
    # 也就是我们要获得parentPt和centerPt，这里一开始两者是相同的
    # 并且我们一开始一个根节点，实际上只要调用plotTree
    firstStr = list(myTree.keys())[0]
    # 这里为什么要写成plotTree.xOff而不是xOff，其实也可以写，但容易报错
    # 这里centerPt怎么来的？首先centerPt的意思是每次传进来如果不是叶子节点，那么需要得到这个父节点的位置
    # 也就是centerPt的位置，xOff的意思是1/叶子总数，再除以二，这样每次加上xOff这样一个间隔，就可以到下一个叶子的x
    # 然后这里的centerPt是需要加上传入进来树的叶子节点
    centerPt = (plotTree.xOff+(1+numLeafs)/2/plotTree.TOTAL_LEAF,plotTree.yOff)
    # 这里根节点是用decisionNode，叶子节点用leafNode(即后面判断不是字典时使用)
    plotNode(nodeTxt,parentPt,centerPt,decisionNode)
    plotMidContent(firstStr,parentPt,centerPt)
    # 也需注意，这里我们直接传入centerPt和parentPt
    # 接下来对根节点后面的内容进行迭代
    secondDict = myTree[firstStr]
    # 迭代时候，y的坐标要下降
    plotTree.yOff -= 1/plotTree.TOTAL_DEPTH
    for key in secondDict.keys():
        if type(secondDict[key]) == dict:
            # 如果是字典，那么直接递归，但要注意传入进去的参数
            # 把secondDict作为新的树，那么自然的现在的centerPt就成为了parentPt(作为新的根节点)
            plotTree(secondDict[key],centerPt,str(key))
        else:
            # 如果不是，那么需要调用plotMidContent和plotTree，并且注意传入的参数
            plotTree.xOff += 1/plotTree.TOTAL_LEAF
            plotMidContent(str(key),centerPt,(plotTree.xOff, plotTree.yOff))
            plotNode(secondDict[key],centerPt,(plotTree.xOff, plotTree.yOff),leafNode)
    plotTree.yOff += 1/plotTree.TOTAL_DEPTH


def createPlot(myTree):
    # 这里的作用就是把一开始的树和根节点传入，然后开始画树
    fig = plt.figure(1,facecolor="white")
    fig.clf()
    createPlot.ax1 = plt.subplot(111,frameon=False)
    # 这里为了与遍历(递归)过程中的叶子节点数目和深度区别，我用大写，表示不变，而numLeafs会动态变化
    plotTree.TOTAL_LEAF = gnn.getNumLeafs(myTree)
    plotTree.TOTAL_DEPTH = gnn.getTreeDepth(myTree)
    plotTree.xOff = -0.5/plotTree.TOTAL_LEAF
    plotTree.yOff = 1.0
    plotTree(myTree,(0.5,1.0),"")
    plt.show()

if __name__ == "__main__":
    myTree = {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}},3:'maybe'}}
    createPlot(myTree)
