# 机器学习实战的代码
# 这是第一个最简单的内容，熟悉字典排序
import numpy as np


# 数据集
def createDataSet():
    dataSet = np.array([[1, 1], [1, 1.2], [0, 0], [0, 0.2]])
    labels = np.array(['A', 'A', 'B', 'B'])
    return dataSet, labels


dataSet, labels = createDataSet()


# print(dataSet)
# print(labels)

# 生成器
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
    for i in range(k):
        label = labels[distances_rank[i]]
        # get函数如果有则正常取，没有则使用后面的参数0
        generate_dict[label] = generate_dict.get(label, 0) + 1
    # 对字典的值进行排序
    sorted_dict = sorted(generate_dict.items(), key=lambda x: x[1], reverse=True)
    print(sorted_dict)
    return sorted_dict[0][0]


predict_x = np.array([0, 0.1])
result = classifier(predict_x, dataSet, labels, 3)
print(result)
