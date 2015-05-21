# -*- coding: utf-8 -*-

import os
import re

class filepath:

    def __init__(self,path):
        '''
        :param path: 根目录
        :return:
        '''
        self.path=path

        #存放根目录、根目录下的所有文件夹、文件夹下的文件夹路径
        self.dir=[]


    def return_filedir(self):
        '''
        返回某一个根目录下所有文件的目录，包括文件夹里面的文件夹目录

        parent存放根目录
        dirnames存放根目录parent下所有的文件夹，没有文件夹就为空
        filenames存放根目录parent下所有的文件名，没有文件名为空
        先运行parent目录，输出一遍dirnames和filenames，接着一个一个深度遍历dirnames中的文件夹，每个文件夹又当做是一个parent
        '''

        #获取每个文件夹路径
        for parent,dirnames,filenames in os.walk(self.path):
            for dirname in dirnames:
                self.dir.append(os.path.join(parent,dirname))

        #如果根目录下没有文件夹，就返回根目录
        if self.dir == []:
            self.dir.append(self.path)

        return self.dir


    def replace_char(self,item):
        '''
        因为刚开始没有考虑 。 这个特殊字符，现在要重新去掉
        :param item:需要处理的句子
        :return:
        '''
        item1 = item
        p = re.compile('。|、|，|《|》|？|～|；')
        item1=re.sub(p,'',item1)
        return item1


    def process_filecontent(self):

        '''
        处理获取到的微博文本中没有name或没有data或data小于10的微博，将这些微博文本直接删除
        :return:
        '''
        print self.dir
        for path in self.dir:
            for filename in os.listdir(path):
                file_path = os.path.join(path,filename)
                f = open(file_path, 'r')
                line = f.readline()

                #去除 。 字符
                # line = self.replace_char(line)

                f.close()

                print line
                #将文本按照 ** 进行分割，前半部分是name，后半部分是data
                line_split = line.split('**')

                print file_path, line, line_split, len(line_split[0].decode('utf-8')), len(line_split[1].decode('utf-8'))

                #将data的内容转成unicode之后再求长度
                if ( line_split[0] == '' ) or ( line_split[1] == '' ) or ( len(line_split[1].decode('utf-8') ) < 10):
                    print '删除了', file_path
                    os.remove(file_path)
                else:
                    line = self.replace_char(line)
                    f = open(file_path, 'w')
                    f.write(line)
                    f.close()


if __name__ == '__main__':
    filedirname = []
    filedir = r'F:\srcText\xinlangweibo'

    fd = filepath(filedir)
    filedirname = fd.return_filedir()
    print filedirname
    print len(filedirname)

    fd.process_filecontent()

    # filecontent = ['你好。','你是不是又改换头像了。']
    # str = filecontent[1].decode('utf-8')
    # print repr(str)
    # print len(str)
