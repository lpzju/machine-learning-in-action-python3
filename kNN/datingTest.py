# 第二份代码，进行txt格式文件的处理

import numpy as np

filename = "./datingTestSet2.txt"
def file2matrix(filename):
    with open(filename,'r')as fobj:
        content_arr = fobj.readlines()
        arr_len = len(content_arr)
        dataSet = np.zeros((arr_len,3))
        labelSet = np.zeros((1000,1))
        index = 0
        for line in content_arr:
            line = line.strip()
            new_line = line.split('\t')
            dataSet[index,:] = new_line[0:3]
            labelSet[index] = int(new_line[-1])
            index += 1
        return dataSet, labelSet

dataSet, labelSet = file2matrix(filename)
if __name__ == "__main__":
    print(labelSet)
