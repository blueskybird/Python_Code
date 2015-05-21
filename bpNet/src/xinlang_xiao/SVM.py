# -*- coding: utf-8 -*-

from sklearn import svm
from featurevec import *
import datetime

print 'start...'
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
    print file_folders[i], len(v)
    for j in v:
        means.append(j)
        classnum.append(i)
print '---', len(means), len(classnum), lena

# clf = svm.SVC()
clf = svm.LinearSVC()
clf.fit(means, classnum)

# X = [[0, 0], [1, 1], [2, 2], [3, 3]]
# Y = [0, 1, 2, 3]
# clf = svm.SVC()
# clf.fit(X, Y) 
# out = clf.predict([[1,0]])
# print out


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
    print file_folders_ts[i], len(v)
    for j in v:
        means_test.append(j)
        classnum_test.append(i)
print '***', len(means_test), len(classnum_test), lena

outt = clf.predict(means_test)

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

sum_zq = 0
sum_zh = 0

print result

for i in result:
    print float(i[0]) / float((i[0] + i[1])), float(i[0]) / float((i[0] + i[2]))
    sum_zq += float(i[0]) / float((i[0] + i[1]))
    sum_zh += float(i[0]) / float((i[0] + i[2]))
  
print '平均准确率为： ', float(sum_zq) / float(len(result))
print '平均召回率为： ', float(sum_zh) / float(len(result))

end_time = datetime.datetime.now()

print end_time - start_time
print 'end...'

# 实验结果
# F:\kuaipan\short_text_data\xilangweibo_test\constellation 547
# F:\kuaipan\short_text_data\xilangweibo_test\economic 376
# F:\kuaipan\short_text_data\xilangweibo_test\food 413
# F:\kuaipan\short_text_data\xilangweibo_test\health 287
# F:\kuaipan\short_text_data\xilangweibo_test\sport 190
# F:\kuaipan\short_text_data\xilangweibo_test\travel 199
# *** 2012 2012 6
# [[531, 15, 16], [357, 47, 19], [386, 13, 27], [258, 36, 29], [167, 3, 23], [181, 18, 18]]
# 0.972527472527 0.970749542962
# 0.883663366337 0.949468085106
# 0.967418546366 0.934624697337
# 0.877551020408 0.898954703833
# 0.982352941176 0.878947368421
# 0.909547738693 0.909547738693
# 平均准确率为：  0.932176847585
# 平均召回率为：  0.923715356059