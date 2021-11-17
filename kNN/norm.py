# 获得数据
import datingTest

dataSet = datingTest.dataSet
labelSet = datingTest.labelSet
# print(labelSet)


def norm(dataSet):
    minVals = dataSet.min(axis=0)
    maxVals = dataSet.max(axis=0)
    # print(minVals)
    # 会进行广播，所以不用像书上用tile函数进行复制
    ranges = maxVals - minVals
    norm_data = (dataSet - minVals) / ranges
    return norm_data, ranges, minVals


norm_data, ranges, minVals = norm(dataSet)
if __name__ == "__main__":
    print(norm_data)
    print(ranges)
    print(minVals)
