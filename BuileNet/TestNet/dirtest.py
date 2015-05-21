# -*- coding: utf-8 -*-
import os
import os.path
# rootdir = r"F:\splitedText"                               # 指明被遍历的文件夹
# rootdir=r'F:\splitedText\zhonghuaNet'
# for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
#     for dirname in  dirnames:                       #输出文件夹信息
#         # print "parent is:" + parent
#         # print "dirname is:" + dirname
#         print "the full path of the files is :"+os.path.join(parent,dirname)

    # for filename in filenames:                        #输出文件信息
    #     print "parent is:" + parent
    #     print "filename is:" + filename
    #     print "the full name of the file is:" + os.path.join(parent,filename) #输出文件路径信息

    # print filenames

a="你好 我好 大家好 你好"
for i in a.strip().split(' '):
    print i

print len(a.split(' ')), a.strip().split(' ')

sp = a.strip().split(' ')
print sp.count('你好')