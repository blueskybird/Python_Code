# -*- coding: utf-8 -*-
from pybrain.datasets            import ClassificationDataSet
from pybrain.utilities           import percentError
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SoftmaxLayer

from pylab import ion, ioff, figure, draw, contourf, clf, show, hold, plot
from scipy import diag, arange, meshgrid, where
from numpy.random import multivariate_normal

from dirmould import *
from otherData import *

#指明被遍历的文件夹
rootdir=r'F:\splitedText\zhonghuaNet'
a=dir(rootdir)
b=vec()

means = []
classnum=[]
#引用otherData的函数做测试
means,classnum=meansandclass()

#引用dirmould的函数
# for i in range(len(a.redir())):
#     v=b.revec(a.redir()[i])
#     for j in v:
#         means.append(j)
#         classnum.append(i)

# alldata = ClassificationDataSet(10, 1, nb_classes=5)
alldata = ClassificationDataSet(len(means[0]), 1, nb_classes=5)

for i in range(len(classnum)):
    alldata.addSample(means[i],classnum[i])
    # alldata.appendLinked(means[i],classnum[i])

tstdata, trndata = alldata.splitWithProportion( 0.25 )


# print tstdata

trndata._convertToOneOfMany( )
tstdata._convertToOneOfMany( )

# print "Number of training patterns: ", len(trndata)
# print "Input and output dimensions: ", trndata.indim, trndata.outdim
# print "First sample (input, target, class):"
# print trndata['input'][0], trndata['target'][0], trndata['class'][0]

fnn = buildNetwork( trndata.indim, 5, trndata.outdim, outclass=SoftmaxLayer )

trainer = BackpropTrainer( fnn, dataset=trndata, momentum=0.1, verbose=True, weightdecay=0.01)

trainer.trainEpochs(epochs=100)

out = fnn.activateOnDataset(tstdata)
print out
print tstdata['target']
# print trndata.outdim
