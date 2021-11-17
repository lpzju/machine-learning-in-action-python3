# 对之前做好的kNN算法进行预测
# 首先获取之前构造好的kNN分类器、数据、规则化之后的数据
import kNN
import norm

# 倒完包之后先别急，目的是从规则化的数据集里面选100个出来，用分类器进行预测，计算错误率
# 这里图简单，直接用的前100个进行预测，后面会打乱数据集进行真正的随机

labelSet = norm.labelSet
norm_data = norm.norm_data
random_ratio = 0.10
norm_num = len(norm_data)  # 1000
predict_num = int(random_ratio * norm_num)  # 100
errorNum = 0.0



# 开始预测
for i in range(predict_num):
    predict_result = kNN.classifier(norm_data[i, :], norm_data[predict_num:norm_num, :], labelSet[predict_num:norm_num], 3)
    # print(predict_result)
    print("the classifier came back with:%d,the real answer is:%d " % (predict_result, labelSet[i]))
    if predict_result != labelSet[i]:
        errorNum += 1.0
print("the total error rate is:%f"%(errorNum/float(predict_num)))


