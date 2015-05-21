# -*- coding: utf-8 -*-
import os
import os.path
import datetime
import math

class FileDir:

    def __init__(self, path):
        self.path = path
        self.dir = []

    def return_filedir(self):
        '''
        返回文件下的子文件夹目录，代表不同的类别
        '''
        for parent, dirnames, filenames in os.walk(self.path):
            for dirname in dirnames:
                self.dir.append(os.path.join(parent, dirname))
        if self.dir == []:
            self.dir.append(self.path)
        return self.dir

class FeatureVec:
    def __init__(self):
        # 存放所有特征词
        self.vecallword = []
        # 存放特征词频，也是在多少个文本中出现过
        self.vecallwordnum = []
        self.__getallword()

    def __getallword(self):
        # 获得所有的特征词
#         f=open(r'/home/lsh/Desktop/wordNum/xinlangweibofeatures.txt','r')
        f = open(r'F:\kuaipan\short_text_data\xinlangweibofeatures.txt', 'r')

        line = f.readline()
        while line:
            spline = line.split(' ')
            # w.write(spline[0]+'\n')
            self.vecallword.append(spline[0].strip())
            self.vecallwordnum.append(spline[1].strip())
            line = f.readline()
        f.close()
        
        print 'length of feature is ', len(self.vecallword)

    
    def return_feature_vec(self, path, gongxian):
        '''
        将path目录下所有的文本序列化成一个矩阵返回
        '''
        vecalltext = []
        for f in os.listdir(path):
            fi = open(os.path.join(path, f), 'r')
            line = fi.readline()
            while line:
                vw = [0] * len(self.vecallword)
                spline = line.strip().split(' ')
                for w in spline:
                    if w in self.vecallword:
                        # 特征词出现的文本数除以文本总数
#                        val=math.log(1*(float(self.totalnum)/float(self.vecallwordnum[self.vecallword.index(w)])))
#                        vw[self.vecallword.index(w)]=val
#                        print val
                        vw[self.vecallword.index(w)] = 1
                        #最大共现的词也赋值为1
                        vw[max(gongxian[self.vecallword.index(w)])] = 1
                vecalltext.append(vw)
                line = fi.readline()
        return vecalltext



if __name__ == '__main__':
    start = datetime.datetime.now()
    
    FD = FileDir(r'/home/lsh/Desktop/xinlangweibo')
    for i in FD.return_filedir():
        print i
        
    FV = FeatureVec()
    
    for i in FV.return_feature_vec(r'/home/lsh/Desktop/xinlangweibo/economic'):
        print i
    
    end = datetime.datetime.now()
    print end - start

