写在开头，打算耐心啃完`机器学习实战`这本书，所用版本为2013年6月第1版
在P19页的实施kNN算法时，有很多地方不懂，遂仔细研究，记录如下：
***
#### 字典按值进行排序
- 首先仔细读完kNN算法之后，了解其是用距离来进行判别
- 程序清单2-1看不太明白，于是把具体的inX，dataSet，labels，k带进去大致明白了意思，这里不做演示
- 书上用字典进行存储，然后对字典的值进行排序，这里不太清楚故去学习了一下

这些理清楚之后，首先来看如何对字典的值进行排序：
```python
dict1 = {'a': 1, 'b': 4, 'c': 2, 'f' : 12}
 
# 第一种方法，key使用lambda匿名函数取value进行排序
a = sorted(dict1.items(),key = lambda x: x[1])
b = sorted(dict1.items(),key = lambda x:x[1],reverse = True)
print(a)
print(b)

[('a', 1), ('c', 2), ('b', 4), ('f', 12)]
[('f', 12), ('b', 4), ('c', 2), ('a', 1)]
```
这里sorted的第一个参数为容器，传入的是items，然后第二个参数选择items的第二个值也就是这里的values

```python
dict1 = {'a': 1, 'b': 4, 'c': 2, 'f' : 12}
 
# 第一种方法，key使用lambda匿名函数取value进行排序
a = sorted(dict1.keys(),key = lambda x: x[0])
b = sorted(dict1.keys(),key = lambda x:x[0],reverse = True)
print(a)
print(b)

['a', 'b', 'c', 'f']
['f', 'c', 'b', 'a']
```

这里请注意第一个参数容器，需和第二个参数key中排序内容对应，不能第一个选values，第二个填x[1]

```python
?sorted

Signature: sorted(iterable, /, *, key=None, reverse=False)
Docstring:
Return a new list containing all items from the iterable in ascending order.

A custom key function can be supplied to customize the sort order, and the
reverse flag can be set to request the result in descending order.
Type:      builtin_function_or_method
```

如果不想使用匿名函数，也可使用itemgetter()函数按第几维进行排序

```python
# 第二种方法使用operator的itemgetter进行排序
import operator
dict1 = {'a': 1, 'b': 4, 'c': 2, 'f' : 12}
c = sorted(dict1.items(), key=operator.itemgetter(1))
print(c)
```
#### kNN算法

在写出完整代码之前，我们还要处理一个问题：

计算出某一具体向量到各数据之间的距离之和，如何按照距离进行排序，再存储进字典中

```python
import numpy as np
def createDataSet():
    dataSet = np.array([[1,1],[1,1.2],[0,0],[0,0.2]])
    labels = np.array(['A','A','B','B'])
    return dataSet,labels
dataSet,labels = createDataSet()
a = np.array([0.1,0.2])-dataSet
a = a**2
a = a.sum(axis=1)
a

array([1.45, 1.81, 0.05, 0.01])
```

即在字典存储时，如何将上述的array按序存入？

```python
numpy.argsort(a, axis=-1, kind=’quicksort’, order=None)
```

使用argsort函数即可

```python
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
```

最后结果

```python
[('B', 2), ('A', 1)]
B
```

