# -*- coding: utf-8 -*-
import os

class WordCount:

    def __init__(self):
        pass

    def file_path(self, path):
        '''
        生成文件路径列表
        :param path:文件所在文件夹目录
        :return: 文件路径列表
        '''
        file_path = []

        filenames = os.listdir(path)

        for filename in filenames:
            file_path.append(os.path.join(path, filename))

        return file_path

    def word_count(self, file_path):
        '''
        将文件内容按照格式分割成name和data两部分，并统计文件里面的词的个数
        统计格式：c,t  非c,t   c,非t   非c，非t   t在c中出现的次数

        :param file_path:某个文件下所有文件路径列表
        :return:返回统计结果，目前返回的是某个类的data统计结果
        '''
        #定义两个变量，一个单独存放data的分词结果，一个存放name和data合在一起的结果
        only_data = {}
        name_and_data = {}

        #加载停用词表
        stopword = []
        f1=open(r'F:\wordNum\StopWord.txt','r')
        stopw=f1.readline().strip()
        while stopw:
            stopword.append(stopw)
            stopw=f1.readline().strip()

        #该类中一共有多少个文件
        filenum = len(file_path)

        for fp in file_path:
            f = open(fp, 'r')
            lines =  f.readline()
            lines_split = lines.split(' * * ')
            line_names = lines_split[0].strip().split(' ')
            line_datas = lines_split[1].strip().split(' ')

            #去停用词
            line_names = [ w for w in line_names if w not in stopword]
            line_datas = [ w for w in line_datas if w not in stopword]

            #统计A，即特征t出现的文本数  c,t
            for s in set(line_datas):
                if only_data.has_key(s):
                    only_data[s][0] += 1
                    only_data[s][2] -= 1
                else:
                    only_data[s] = [1,0,filenum - 1,0,0]

            #统计n,即特征t在类c里面出现的次数   t在c中出现的次数
            for data in line_datas:
                if only_data.has_key(data):
                    only_data[data][4] += 1

        return only_data


if __name__ == '__main__':
    '''
    本文件的作用是将新浪微博的七个类中每个类的特征项统计在一个文件中，为CHI.py的计算做准备
    '''
    root_file_path = r'F:\splitedText\xinlangweibo'
    for fp in os.listdir(root_file_path):
        file_name = fp + 'WordCount'
        f = open(r'F:\wordNum\xinlangweibowordnum\\' + file_name + '.txt', 'w')
        file_path = os.path.join(root_file_path, fp)
        wc = WordCount()
        file_paths = wc.file_path(file_path)
        data = wc.word_count(file_paths)
        for k, v in data.iteritems():
            # print k,v
            f.write(k + ' ')
            for i in v:
                f.write(str(i) + ' ')
            f.write('\n')
        f.close()

    # a = {'a':[1,2,4],'b':[1,2,5]}
    # f = open(r'F:\wordNum\test.txt', 'w')
    # for k, v in a.iteritems():
    #     print k, v
    #     f.write(k + ' ')
    #     for i in v:
    #         f.write(str(i) + ' ')
    #     f.write('\n')
    # f.close()