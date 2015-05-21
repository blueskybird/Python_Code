# -*- coding: utf-8 -*-

import urllib2
import re


class xinlangweibo_spider:

    def __init__(self):
        '''
        初始化self.data和self.name变量，其中
        self.data存储微博内容
        self.name存储发微博的名字
        '''
        self.data = []

        self.name = []

    def replace_char(self, item):
        '''
        去除获得的文本中的不必要的标点字符
        '''

        item1 = item

        # p = re.compile('\d+|”|“| |:|：|\(|\)|-|/|（|）|\\\\|%|\?|\[|\]|\#|\&|\*|\{|\}|\||\.|\w|，|＂|＂|》|《|<|=|>|"|、|？|’|‘|!|;|·|•|\+|,|~|！|３|…|【|】|。|é|з|ゝ|∠')
        #这里去掉一些字符是考虑到这些字符对分词可能有一定帮助，比如：。 、 ， 《 》等。明天需要测试下分词  《天下有情人》和天下有情人  的分词结果
        p = re.compile('\d+|”|“| |:|：|\(|\)|-|/|（|）|\\\\|%|\?|\[|\]|\#|\&|\*|\{|\}|\||\.|\w|＂|＂|<|=|>|"|’|‘|!|;|·|•|\+|,|~|！|３|…|【|】|é|з|ゝ|∠')
        item1=re.sub(p,'',item1)

        return item1


    def save_data(self, url, filename):
        '''
        将最后获得的文本保存在指定目录下
        :param url: 要爬取的网址
        :param filename: 将url内容放到对应的文件夹中
        :return:没有返回值
        '''

        # print url

        # self.get_data(url)

        title = 1

        length = len(self.data) #len(self.name)长度一样
        print length

        for i in range(length):
            til = '%d' %title
            f=open(r'F:\srcText\xinlangweibo\\'+filename +'\\'+ til+ '.txt','w')
            #将用户名与微博内容隔开
            f.write(self.name[i] + '**' + self.data[i])
            f.close()
            title += 1


    def get_data(self, url):
        '''
        读取指定的url中的内容
        :param url要爬去的网址:
        :return:没有返回值
        '''
        #新浪微博写的是采用utf-8解码

        myPage = urllib2.urlopen(url).read().decode('utf-8')
        self.deal_data(myPage)


    def deal_data(self, myPage):
        '''
        通过正则获取myPage中自己需要的内容
        :param myPage:读到的网页内容
        :return:没有返回值
        '''

        item_data = re.findall(r'node-type=\\"feed_list_content\\">(.*?)<', myPage, re.S)
        item_name = re.findall(r'nick-name=\\"(.*?)\\"', myPage, re.S)

        for item in item_data:
            #如果不encode的话，item是unicode格式，没法进行下面的去除字符串处理
            it = item.encode('utf-8')
            # print it
            item1 = self.replace_char(it)
            self.data.append(item1)
            # print item1

        for item in item_name:
            it = item.encode('utf-8')
            # print it
            item1 = self.replace_char(it)
            self.name.append(item1)
            # print item1

        for i in range(len(self.name)):
            print self.name[i],'**',self.data[i]



# if __name__ == '__main__':
#
#     index = 1
#     url = r'http://d.weibo.com/102803_ctg1_1399_-_ctg1_1399?current_page=1&since_id=&page=%d#feedtop' %index