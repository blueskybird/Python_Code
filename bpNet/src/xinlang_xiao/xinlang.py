# -*- coding: utf-8 -*-
from pybrain.datasets import ClassificationDataSet
from pybrain.datasets import SupervisedDataSet
from pybrain.utilities import percentError
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import SoftmaxLayer

# from pylab import ion, ioff, figure, draw, contourf, clf, show, hold, plot
from scipy import diag, arange, meshgrid, where
from numpy.random import multivariate_normal

import datetime
import os
import sys
from featurevec import *

print 'begin....'
start=datetime.datetime.now()

#train data
# rootdir = r'/home/lsh/Desktop/xinlangweibo'
rootdir = r'F:\kuaipan\short_text_data\xinlangweibo'
fd = FileDir(rootdir)
file_folders = fd.return_filedir()

fv = FeatureVec()
 
means = []
classnum=[]

lena=len(file_folders)
for i in range(lena):
    v=fv.return_feature_vec(file_folders[i])
    for j in v:
        means.append(j)
        classnum.append(i)


alldata = ClassificationDataSet(len(means[0]), 1, nb_classes=7)
#alldata = SupervisedDataSet(len(means[0]),1)

le=len(classnum)
j=0
print le
for i in xrange(le):
    alldata.addSample(means[i],classnum[i])
    j+=1
    print classnum[i],len(means[i]),j
#    alldata.appendLinked(means[i],classnum[i])

#trndata, tstdata = alldata.splitWithProportion(0.75)
trndata = alldata
 
#test data
# rootdir_test=r'/home/lsh/Desktop/xilangweibo_test'
rootdir_test = r'F:\kuaipan\short_text_data\xilangweibo_test'
fd = FileDir(rootdir_test)
file_folders_ts = fd.return_filedir()

fv = FeatureVec()
 
means_test = []
classnum_test=[]

lena=len(file_folders_ts)
for i in range(lena):
    v=fv.return_feature_vec(file_folders_ts[i])
    for j in v:
        means_test.append(j)
        classnum_test.append(i)


alldata_test = ClassificationDataSet(len(means[0]), 1, nb_classes=7)
#alldata = SupervisedDataSet(len(means[0]),1)

le=len(classnum_test)
j=0
print le
for i in xrange(le):
    alldata_test.addSample(means_test[i],classnum_test[i])
    j+=1
    print classnum_test[i],len(means_test[i]),j
#    alldata.appendLinked(means[i],classnum[i])

#trndata, tstdata = alldata.splitWithProportion(0.75)
tstdata = alldata_test

trndata._convertToOneOfMany()
tstdata._convertToOneOfMany()

fnn = buildNetwork( trndata.indim, 7, trndata.outdim, outclass=SoftmaxLayer )

trainer = BackpropTrainer(fnn, dataset=trndata, momentum=0.1, batchlearning=True, verbose=True, weightdecay=0.01)

trainer.trainEpochs(epochs=1800)
 
out = fnn.activateOnDataset(tstdata)

shuchu=[]
#正确分类该类的文本数、错误分到其他类的文本数、其他类分到该类中的文本数
#result=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
result=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]


list_out=out.tolist()
list_tstdata=tstdata['target'].tolist()

for i in list_out:
    print i
    
for i in list_tstdata:
    print i
    
for i in range(len(list_out)):
    #分错的
    if list_out[i].index(max(list_out[i])) != list_tstdata[i].index(max(list_tstdata[i])):
        result[list_tstdata[i].index(max(list_tstdata[i]))][1] += 1
        result[list_out[i].index(max(list_out[i]))][2] += 1
    else:
        result[list_tstdata[i].index(max(list_tstdata[i]))][0] += 1
        
print result

for i in range(len(file_folders)):
    print file_folders[i], file_folders_ts[i]

sum_zq = 0
sum_zh = 0

for i in result:
    print float(i[0])/float((i[0]+i[1])),float(i[0])/float((i[0]+i[2]))
    sum_zq += float(i[0])/float((i[0]+i[1]))
    sum_zh += float(i[0])/float((i[0]+i[2]))

print '平均准确率为： ', float(sum_zq)/float(len(result))
print '平均召回率为： ', float(sum_zh)/float(len(result))


print 'end....'
end=datetime.datetime.now()
print end-start