from pybrain.datasets import ClassificationDataSet
from pybrain.utilities import percentError
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import SoftmaxLayer

# from pylab import ion, ioff, figure, draw, contourf, clf, show, hold, plot
from scipy import diag, arange, meshgrid, where
from numpy.random import multivariate_normal

import datetime

from dirmould import *

print 'begin....'
start=datetime.datetime.now()
rootdir=r'/home/lsh/Desktop/splitedText/zhonghuaNet'
a=dir(rootdir)
b=vec()
 
means = [[0,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]
classnum=[0,1,2,3,4]

alldata = ClassificationDataSet(5, 1, nb_classes=5)
#alldata = ClassificationDataSet(len(means[0]), 1, nb_classes=5)

for i in range(20):
    for j in range(5):
        alldata.addSample(means[j],classnum[j])
#        alldata.appendLinked(means[j],classnum[j])
 
tstdata, trndata = alldata.splitWithProportion( 0.25 )

# print tstdata

trndata._convertToOneOfMany()
tstdata._convertToOneOfMany()
  
#print "Number of training patterns: ", len(trndata)
#print "Input and output dimensions: ", trndata.indim, trndata.outdim
#print "First sample (input, target, class):"
#print trndata['input'][0], trndata['target'][0], trndata['class'][0]
fnn = buildNetwork( trndata.indim, 5, trndata.outdim, outclass=SoftmaxLayer )

trainer = BackpropTrainer( fnn, dataset=trndata, momentum=0.1, verbose=True, weightdecay=0.01)

trainer.trainEpochs(epochs=100)
 
out = fnn.activateOnDataset(tstdata)
for i in out:
    print i
for i in tstdata['target']:
    print i
#print out,tstdata['target']
print 'end....'
end=datetime.datetime.now()
print end-start
# print trndata.outdim