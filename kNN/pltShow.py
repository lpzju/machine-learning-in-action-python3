# 导包
import datingTest
import matplotlib.pyplot as plt
import numpy as np

# 获得数据
dataSet = datingTest.dataSet
labelSet = datingTest.labelSet

# 获得画布
fig = plt.figure()
# 子图，111表示1行1列第一张图
ax = fig.add_subplot(111)
# 画点图
ax.scatter(dataSet[:,1],dataSet[:,2],15.0*np.array(labelSet),15.0*np.array(labelSet))
# 标签
plt.xlabel("Percentage of time spent playing video games")
plt.ylabel("The number of liters of ice cream consumed per week")
# plt.subplot(111)
# plt.scatter(dataSet[:,1],dataSet[:,2])
# 这里千万要注意，savefig要放在show之前，因为show调用完之后，会是另外的画图工作，此时savefig会是白板
plt.show()
plt.savefig("./datingImg1.jpg")
