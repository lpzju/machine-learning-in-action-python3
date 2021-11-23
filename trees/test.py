import matplotlib.pyplot as plt

decisionNode = dict(boxstyle="sawtooth",fc="0.8")
leafNode = dict(boxstyle="round4",fc="0.8")
arrow_args = dict(arrowstyle="<-")

def plotNode(nodeTxt,centerPt,parentPt,nodeType):
    createNode.ax1.annotate(nodeTxt,xy=parentPt,xytext=centerPt,bbox=nodeType,arrowprops=arrow_args)

def createNode():
    fig = plt.figure(1,facecolor="white")
    fig.clf()
    createNode.ax1 = plt.subplot(111,frameon=False)
    plotNode("kkk",(0.7,0.1),(0.3,0.7),decisionNode)
    plotNode("lll",(0.8,0.2),(0.2,0.5),leafNode)
    plt.show()

createNode()