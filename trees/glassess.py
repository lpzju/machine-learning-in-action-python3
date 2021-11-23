import plot_all
import trees_together
with open('lenses.txt') as fobj:
    lenses = [line.strip().split('\t') for line in fobj.readlines()]
    lensesLabels = ['age','prescript','astigmatic','tearRate']
    lensesTree = trees_together.createTree(lenses,lensesLabels)
    # print(lensesTree)
    plot_all.createPlot(lensesTree)