from dirmould import *
from pybrain.datasets import ClassificationDataSet

start=datetime.datetime.now()
rootdir=r'/home/lsh/Desktop/splitedText/zhonghuaNet'
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

tstdata=ClassificationDataSet(len(means[0]),1,nb_classes=10)

rootdirtest=r'/home/lsh/Desktop/splitedText/zhonghuaNetTest'
at=dir(rootdirtest)
bt=vec()

fat=at.redir()
lena=len(fat)

out=[]

print '***'
print lena
print '***'

for i in range(lena):
    v=bt.revec(fat[i])
    for j in v:
        otmp=[]
        tstdata.clear()
        tstdata.addSample(j, i)
        
print '---'
for i in tstdata['input']:
    print i
print '---'
for i in tstdata['target']:
    print i

print '---'
print tstdata