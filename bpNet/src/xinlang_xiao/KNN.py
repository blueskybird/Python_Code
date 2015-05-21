# -*- coding: utf-8 -*-

from sklearn import neighbors
import numpy as np
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


knn = neighbors.KNeighborsClassifier(lena)

# x = [[0, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1]]
# y = [0, 1, 1, 2, 2]
# knn.fit(x, y)

knn.fit(means, classnum)


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

# p = [[0, 1, 1, 1]]
# 
# print knn.predict(p)
# print knn.predict_proba(p)

outt = knn.predict(means_test)
outp = knn.predict_proba(means_test)
print '---', outt, len(outt)

shuchu = []
out_list = outt.tolist()
list_tstdata = classnum_test
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
 
for i in range(len(out_list)):
    # 分错的
    if out_list[i] != classnum_test[i]:
        result[classnum_test[i]][2] += 1
        result[out_list[i]][1] += 1
    else:
        result[classnum_test[i]][0] += 1
        
# for i in range(len(out_list)):
#     #分错的
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
 
print '平均准确率为： ', float(sum_zq) / float(len(result))
print '平均召回率为： ', float(sum_zh) / float(len(result))


end_time = datetime.datetime.now()
print end_time - start_time
print 'end'

# 实验结果：
# 0.976377952756 0.453382084095
# 0.355212355212 0.978723404255
# 0.754966887417 0.82808716707
# 0.889763779528 0.393728222997
# 1.0 0.0157894736842
# 0.827338129496 0.577889447236
# 平均准确率为：  0.800609850735
# 平均召回率为：  0.541266633223
