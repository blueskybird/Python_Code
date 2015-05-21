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

#指明被遍历的文件夹
# rootdir=r'F:\splitedText\zhonghuaNet'
# rootdir=r'F:\TrainTest\Test'
rootdir=r'F:\TrainTest\Train'
a=dir(rootdir)
b=vec()

means = []
classnum=[]

# f=open(r'F:\totaldata.txt','w')
# f=open(r'C:\Users\Administrator\Desktop\tsdata.txt','w')
# f1=open(r'C:\Users\Administrator\Desktop\tstarget.txt','w')
f=open(r'C:\Users\Administrator\Desktop\trdata.txt','w')
f1=open(r'C:\Users\Administrator\Desktop\trtarget.txt','w')

for i in range(len(a.redir())):
    v=b.revec(a.redir()[i])
    print a.redir()[i]
    for j in v:
        for w in j:
            f.write(str(w)+'    ')
            # f.write('    ')
        f1.write(str(i)+'\n')

# f=open(r'F:\totaldata.txt','r')
# for i in range(5):
#     print f.readline()

f.close()
f1.close()