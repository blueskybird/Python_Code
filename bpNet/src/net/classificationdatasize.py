# -*- coding: utf-8 -*-
from pybrain.datasets import ClassificationDataSet
from pybrain.utilities import percentError
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import SoftmaxLayer

# from pylab import ion, ioff, figure, draw, contourf, clf, show, hold, plot
from scipy import diag, arange, meshgrid, where
from numpy.random import multivariate_normal

import datetime
import time
import random
import os
import sys
from dirmould import *

print 'begin....'
start=datetime.datetime.now()
rootdir=r'/home/lsh/Desktop/splitedText/zhonghuaNet'
a=dir(rootdir)
b=vec()
 
means = []
classnum=[1,0]

alldata = ClassificationDataSet(14000,1,nb_classes=10)

for i in xrange(7000):
    a=[0]*14000
    l=random.randint(0,14000-1)
    a[l]=1
    means.append(a)
    #最多添加4093个左右，再多就报错了
    alldata.addSample(means[i],classnum[0])
    print classnum[0],len(means[i]),i
#    alldata.appendLinked(means[i],classnum[i])

#tstdata, trndata = alldata.splitWithProportion(0.4)
#trndata, tstdata = alldata.splitWithProportion(0.75)
# 
##print tstdata
#
#trndata._convertToOneOfMany()
#tstdata._convertToOneOfMany()
#
#
#fnn = buildNetwork( trndata.indim, 7, trndata.outdim, outclass=SoftmaxLayer )
#
#trainer = BackpropTrainer(fnn, dataset=trndata, momentum=0.1, batchlearning=True, verbose=True, weightdecay=0.01)
#
#trainer.trainEpochs(epochs=500)
# 
#out = fnn.activateOnDataset(tstdata)