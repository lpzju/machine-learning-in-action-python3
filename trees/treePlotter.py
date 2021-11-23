import matplotlib.pyplot as plt
# boxstyle是文本框类型 fc是边框粗细 sawtooth是锯齿形
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")
# annotate 注释的意思
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    # nodeTxt为要显示的文本，centerPt为文本的中心点，parentPt为箭头指向文本的点，
    # xy是箭头尖的坐标，xytest设置注释内容显示的中心位置
    # xycoords和textcoords是坐标xy与xytext的说明（按轴坐标），
    # 若textcoords=None，则默认textcoords与xycoords相同，若都未设置，默认为data
    # va/ha设置节点框中文字的位置，va为纵向取值为(u'top', u'bottom', u'center', u'baseline')，
    # ha为横向取值为(u'center', u'right', u'left')
    createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction',
                            xytext=centerPt, textcoords='axes fraction',
                            va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)
def createPlot():
    # 1是编号,这里删了也不影响
    fig = plt.figure(1,facecolor='white')  # 新建一个画布，背景设置为白色的
    fig.clf()  # 将画图清空
    createPlot.ax1 = plt.subplot(111, frameon=False)  # 设置一个多图展示，但是设置多图只有一个
    plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)
    plt.show()
createPlot()