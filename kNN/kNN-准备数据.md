在上一小节，我们大概了解了kNN算法的基本原理，现在我们要进行数据的处理

本小节所用数据集来自[机器学习实战]:[Machine Learning in Action (manning.com)](https://www.manning.com/books/machine-learning-in-action)

下载数据集后，将`datingTestSet2.txt`和`datingTestSet`放在本程序同一文件夹下

***

首先阅读程序清单2-2，知道我们应该将`datingTestSet2.txt`文件中的内容进行读取，书上虽然写的是`datingTestSet`，但我们将这两个文件打开之后会发现，2对应的文件是将label进行处理的，而另一个没有。关于数据集处理，博主暂时只会pandas处理，这里用的numpy

#### 读取文件

读取文件`程序清单2-2`直接用的open，没有close，我这里用with open语句

```python
filename = './datingTestSet2.txt'
with open(filename,'r')as fobj:
    content_arr = fobj.readlines()
    print(content_arr)
    
['40920\t8.326976\t0.953952\t3\n', '14488\t7.153469\t1.673904\t2\n', '26052\t1.441871\t0.805124\t1\n',...]
```

#### 创建空的numpy矩阵

目的是将刚刚得到的文件内容，存储到numpy中，这时需要：

1. 上述数据是1000\*4，所以需要有一个1000\*4的ndarray
2. 将刚刚得到的content_arr分开，把回车与换行去掉
3. 1000*4并不能满足我们数据集与标记的需求，所以我们细分成1000\*3的数据，和1000\*1的标记

```python
import numpy as np
filename = "./datingTestSet2.txt"
def file2matrix(filename):
    # 'r'的意思是只读，fobj是file_object的缩写
    with open(filename,'r')as fobj:
        content_arr = fobj.readlines()
        # 获取content_arr的长度
        arr_len = len(content_arr)
        # 构造1000*3的ndarray
        dataSet = np.zeros([arr_len,3])
        # 标记
        labelSet = []
        index = 0
        for line in content_arr:
            # 去掉换行
            new_line = line.strip()
            # 去掉制表
            normal_line = new_line.split('\t')
            # 这时我们再将normal_line存储进dataSet,并将最后一列存进labelSet
            dataSet[index,:] = normal_line[0:3]
            labelSet.append(int(normal_line[-1]))
            index += 1
        return dataSet,labelSet
```

```python
dataSet,labelSet = file2matrix(filename)
dataSet

array([[4.0920000e+04, 8.3269760e+00, 9.5395200e-01],
       [1.4488000e+04, 7.1534690e+00, 1.6739040e+00],
       [2.6052000e+04, 1.4418710e+00, 8.0512400e-01],
       ...,
       [2.6575000e+04, 1.0650102e+01, 8.6662700e-01],
       [4.8111000e+04, 9.1345280e+00, 7.2804500e-01],
       [4.3757000e+04, 7.8826010e+00, 1.3324460e+00]])
```

这里`dataSet[index,:] = normal_line[0:3]`，这样的语法没见到过，这时numpy中的数据处理方式

见下：

```python
import numpy as np
a = np.zeros((5,6))
b = np.array([1,2,3])
print("a:\n",a)
print("b:\n",b)

a:
 [[0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0.]]
b:
 [1 2 3]
```

```python
a[2,3:6] = b
print("a:\n",a)

a:
 [[0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 1. 2. 3.]
 [0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0.]]
```

