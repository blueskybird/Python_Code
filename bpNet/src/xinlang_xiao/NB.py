# -*- coding: utf-8 -*-
from sklearn.naive_bayes import GaussianNB
from featurevec import *
import datetime

start_time = datetime.datetime.now()
# train data
rootdir = r'F:\kuaipan\short_text_data\xinlangweibo'
fd = FileDir(rootdir)
file_folders = fd.return_filedir()
 
fv = FeatureVec()
  
means = []
classnum = []
 
lena = len(file_folders)
for i in range(lena):
    v = fv.return_feature_vec(file_folders[i])
    for j in v:
        means.append(j)
        classnum.append(i)
print len(means), len(classnum), lena

gnb = GaussianNB()
gnb.fit(means, classnum)


# test data
# rootdir_test=r'/home/lsh/Desktop/xilangweibo_test'
rootdir_test = r'F:\kuaipan\short_text_data\xilangweibo_test'
fd = FileDir(rootdir_test)
file_folders_ts = fd.return_filedir()

fv = FeatureVec()
 
means_test = []
classnum_test = []

lena = len(file_folders_ts)
for i in range(lena):
    v = fv.return_feature_vec(file_folders_ts[i])
    for j in v:
        means_test.append(j)
        classnum_test.append(i)

outt = gnb.predict(means_test)


shuchu = []
out_list = outt.tolist()
list_tstdata = classnum_test
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
 
for i in range(len(out_list)):
    # �ִ��
    if out_list[i] != classnum_test[i]:
        result[classnum_test[i]][2] += 1
        result[out_list[i]][1] += 1
    else:
        result[classnum_test[i]][0] += 1
        
# for i in range(len(out_list)):
#     #�ִ��
#     if out_list[i].index(max(out_list[i])) != list_tstdata[i].index(max(list_tstdata[i])):
#         result[list_tstdata[i].index(max(list_tstdata[i]))][1] += 1
#         result[out_list[i].index(max(out_list[i]))][2] += 1
#     else:
#         result[list_tstdata[i].index(max(list_tstdata[i]))][0] += 1

sum_zq = 0
sum_zh = 0
 
for i in result:
    print float(i[0]) / float((i[0] + i[1])), float(i[0]) / float((i[0] + i[2]))
    sum_zq += float(i[0]) / float((i[0] + i[1]))
    sum_zh += float(i[0]) / float((i[0] + i[2]))
 
print '平均准确率为：', float(sum_zq) / float(len(result))
print '平均召回率为：', float(sum_zh) / float(len(result))

end_time = datetime.datetime.now()
print end_time - start_time
print 'end'

# 实验结果
# 0.851351351351 0.921389396709
# 0.863184079602 0.922872340426
# 0.952095808383 0.769975786925
# 0.673076923077 0.853658536585
# 0.958823529412 0.857894736842
# 0.773333333333 0.582914572864
# 平均准确率为：  0.845310837526
# 平均召回率为：  0.818117561725