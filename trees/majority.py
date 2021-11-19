# 这里的代码作用是，如果到了叶子结点，但是还是不能区分
# 比如图3-2上面叶子结点要么都是yes要么都是no，但如果叶子结点上面是yes、yes、no，我们需要一个函数
# 来把这个叶子结点标记为yes，这就是majorityCnt函数的作用
import featureSelect

dataSet = featureSelect.dataSet
labelSet = featureSelect.labelSet

def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        # 这里写法不同，意思是一样的
        # 即如果不在字典中，那么先初始化为0，再+1
        if vote not in classCount:
            classCount[vote] = 0
        classCount[vote] += 1
    # 对于字典排序，书上的方法有点过时了，这里我选择使用匿名函数
    sortedClassCount = sorted(classCount.items(),key=lambda x:x[1],reverse=True)
    return sortedClassCount[0][0]

if __name__ == "__main__":
    classList = ['no','yes','yes']
    result = majorityCnt(classList)
    print(result)