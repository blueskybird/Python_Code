# -*- coding: utf-8 -*-
import os
import os.path
import datetime

class dir:

    def __init__(self,path):
        self.path=path
        self.dir=[]

    def redir(self):
        for parent,dirnames,filenames in os.walk(self.path):
            for dirname in dirnames:
                self.dir.append(os.path.join(parent,dirname))
        if self.dir==[]:
            self.dir.append(self.path)
        return self.dir

class vec:
    def __init__(self):
        #存放所有特征词
        self.vecallword=[]
        #存放特征词频，也是在多少个文本中出现过
        self.vecallwordnum=[]
        #文本总数
        self.totalnum=4026
        self.getallword()

    def getallword(self):
        #获得所有的特征词
        f=open(r'F:\wordNum\wordCount.txt','r')

        #获取停用词表
        f1=open(r'F:\wordNum\StopWord.txt','r')
        stopword=[]
        stopw=f1.readline().strip()#.decode('utf-8')
        while stopw:
            stopword.append(stopw)
            stopw=f1.readline().strip()

        line=f.readline()
        while line:
            spline=line.split(' : ')
            # w.write(spline[0]+'\n')
            self.vecallword.append(spline[0].strip())
            self.vecallwordnum.append(spline[1].strip())
            line=f.readline()
        f.close()

        self.vecallword=[w for w in self.vecallword if w not in stopword]

        print len(self.vecallword),len(self.vecallwordnum)
        for i in range(10):
            print self.vecallword[i], self.vecallwordnum[i]

    #将某个目录下所有的文本序列化成一个矩阵
    def revec(self,path):
        vecalltext=[]
        for f in os.listdir(path):
            fi=open(os.path.join(path,f),'r')
            line=fi.readline()
            while line:
                vw=[0]*len(self.vecallword)
                spline=line.strip().split(' ')
                for w in spline:
                    if w in self.vecallword:
                        #特征词出现的文本数除以文本总数
                        vw[self.vecallword.index(w)]=1*(float(self.vecallwordnum[self.vecallword.index(w)])/float(self.totalnum))
                vecalltext.append(vw)
                line=fi.readline()
        return vecalltext


if __name__=='__main__':
    start=datetime.datetime.now()

    # 指明被遍历的文件夹
    rootdir=r'F:\splitedText\zhonghuaNet'

    a=dir(rootdir)
    b=vec()


    # nb_class=[]
    # alltextvec=[]
    # # for i in  range(len(a.redir())):
    # #     print a.redir()[i]
    # for i in range(len(a.redir())):
    #     v=b.revec(a.redir()[i])
    #     for j in v:
    #         alltextvec.append(j)
    #         nb_class.append(i)
    # print nb_class
    # print len(nb_class),len(alltextvec)
    # print len(alltextvec[0])
    #
    # end=datetime.datetime.now()
    #
    # print end-start