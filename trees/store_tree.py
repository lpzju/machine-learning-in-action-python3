def storeTree(inputTree,filename):
    import pickle
    with open(filename,'wb')as fobj:
        pickle.dump(inputTree,fobj)

def grabTree(filename):
    import pickle
    with open(filename,'rb')as fobj:
        return pickle.load(fobj)

if __name__ == "__main__":
    import trees_together
    dataSet = trees_together.dataSet
    labelSet = trees_together.labelSet
    myTree = trees_together.createTree(dataSet,labelSet)
    storeTree(myTree,'classifierStorage.txt')
    print(grabTree('classifierStorage.txt'))
