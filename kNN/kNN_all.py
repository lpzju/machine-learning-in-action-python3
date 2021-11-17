import numpy as np

filename = "./datingTestSet2.txt"


def file2matrix(filename):
    with open(filename, 'r') as fobj:
        content_arr = fobj.readlines()
        arr_len = len(content_arr)
        dataSet = np.zeros((arr_len, 3))
        labelSet = np.zeros((1000, 1))
        index = 0
        for line in content_arr:
            line = line.strip()
            new_line = line.split('\t')
            dataSet[index, :] = new_line[0:3]
            labelSet[index] = int(new_line[-1])
            index += 1
        return dataSet, labelSet


dataSet, labelSet = file2matrix(filename)

def norm(dataSet):
    minVals = dataSet.min(axis=0)
    maxVals = dataSet.max(axis=0)
    # print(minVals)
    # 会进行广播，所以不用像书上用tile函数进行复制
    ranges = maxVals - minVals
    norm_data = (dataSet - minVals) / ranges
    return norm_data, ranges, minVals


norm_data, ranges, minVals = norm(dataSet)
random_ratio = 0.10
norm_num = len(norm_data)  # 1000
predict_num = int(random_ratio * norm_num)  # 100
errorNum = 0.0


def classifier(arr, dataSet, labels, k):
    new_arr = arr - dataSet
    # return(new_arr)
    new_arr_sqaure = new_arr ** 2
    new_arr_sum = new_arr_sqaure.sum(axis=1)
    # 欧氏距离，先用目标与数据集的每条相减，再平方再求和再开根号
    distances = new_arr_sum ** 0.5
    # return distances
    # 距离进行排序，这样就能知道传入的向量与数据集中的哪个向量最近
    distances_rank = distances.argsort()
    # return distances_rank
    generate_dict = {}
    for j in range(k):
        # print(j)
        label = labels[distances_rank[j]]
        # get函数如果有则正常取，没有则使用后面的参数0
        # print(type(str(label)))
        label = int(label)
        generate_dict[label] = generate_dict.get(label, 0) + 1
    # 对字典的值进行排序
    sorted_dict = sorted(generate_dict.items(), key=lambda x: x[1], reverse=True)
    # print(sorted_dict)
    return sorted_dict[0][0]


# 开始预测
for i in range(predict_num):
    labels1 = (tuple(norm_data[predict_num:norm_num, :]))
    predict_result = classifier(np.array(norm_data[i, :]), labels1,
                                np.array(labelSet[predict_num:norm_num]), 3)
    print("the classifier came back with:%d,the real answer is:%d " % (predict_result, labelSet[i]))
    if predict_result != labelSet[i]:
        errorNum += 1.0
print("the total error rate is:%f" % (errorNum / float(predict_num)))
