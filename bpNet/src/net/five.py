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
from dirmould import *

print 'begin....'
start=datetime.datetime.now()
rootdir=r'E:\short_text\splitedText\zhonghuaNet'
a=dir(rootdir)
b=vec()
 
means = []
classnum=[]

fa=a.redir()
lena=len(fa)
for i in range(lena):
    v=b.revec(fa[i])
    for j in v:
        means.append(j)
        classnum.append(i)

#f=open(r'/home/lsh/Desktop/totaldata.txt','w')

# alldata = ClassificationDataSet(10, 1, nb_classes=5)
#alldata = ClassificationDataSet(len(means[0]), 1, nb_classes=10)
alldata = ClassificationDataSet(len(means[0]),1,nb_classes=10)
#alldata = SupervisedDataSet(len(means[0]),1)

le=len(classnum)
j=0
print le
for i in xrange(le):
    alldata.addSample(means[i],classnum[i])
    j+=1
    print classnum[i],len(means[i]),j
#    alldata.appendLinked(means[i],classnum[i])

#tstdata, trndata = alldata.splitWithProportion(0.4)
trndata, tstdata = alldata.splitWithProportion(0.75)
 
#print tstdata

trndata._convertToOneOfMany()
tstdata._convertToOneOfMany()
  
#print "Number of training patterns: ", len(trndata)
#print "Input and output dimensions: ", trndata.indim, trndata.outdim
#print "First sample (input, target, class):"
#print trndata['input'][0], trndata['target'][0], trndata['class'][0]


fnn = buildNetwork( trndata.indim, 7, trndata.outdim, outclass=SoftmaxLayer )

trainer = BackpropTrainer(fnn, dataset=trndata, momentum=0.1, batchlearning=True, verbose=True, weightdecay=0.01)

trainer.trainEpochs(epochs=10)
 
out = fnn.activateOnDataset(tstdata)

shuchu=[]
#每种分类的正确分类和错误分类数
result=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
#for i in out:
#    l=[0]*5
#    l[i.index(max(i))]=1
#    shuchu.append(l)
#for i in range(5):
#    if shuchu[i]!=tstdata['target'][i]:
#        result[max(tstdata['target'][i])][1]+=1
#    else:
#        result[max(tstdata['target'][i])][0]+=1

#print result

#print out,tstdata['target']

#for i in out:
#    print i
#for i in tstdata['target']:
#    print i

list_out=out.tolist()
list_tstdata=tstdata['target'].tolist()

for i in list_out:
    print i
    
for i in list_tstdata:
    print i


print 'end....'
end=datetime.datetime.now()
print end-start
print trndata.outdim