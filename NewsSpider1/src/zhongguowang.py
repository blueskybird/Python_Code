# -*- coding: utf-8 -*-

import urllib
import re


class zhongguowang_spider:

    def __init__(self):
        self.data=[]

    def replace_char(self,item):
        item1=item
        p = re.compile('\d+|”|“| |:|：|\(|\)|-|/|（|）|\\\\|%|\?|\[|\]|\#|\&|\*|\{|\}|\||\.|\w|，|＂|＂|》|《|<|=|>|"|、|？|’|‘|!|;|·|•|\+|,|~|！|３|…')
        item1=re.sub(p,'',item1)
        return item1

    def save_data(self,url):
        self.get_data(url)
        title=451
        for item in self.data:
            til='%d' %title
            # f=open(r'F:\srcText\zhongguoNet\football\\' + til+ '.txt','w')
            # f=open(r'F:\srcText\zhongguoNet\health\\' + til+ '.txt','w')
            # f=open(r'F:\srcText\zhongguoNet\car\\' + til+ '.txt','w')
            # f=open(r'F:\srcText\renminNet\game\\' + til+ '.txt','w')
            f=open(r'F:\srcText\renminNet\house\\' + til+ '.txt','w')
            f.write(item)
            f.close()
            title+=1

    def get_data(self,url):
        #人民网网页是双重的，先要用GBK解码，然后再用utf-8解码
        myPage=urllib.urlopen(url).read().decode('GBK')
        myPage=myPage.decode('utf-8')
        self.deal_data(myPage)

    def deal_data(self,myPage):
        #足球
        # items=re.findall(r'rel="external">(.*?)</a></li>',myPage,re.S)
        #健康
        # items=re.findall(r'\.htm">(.*?)</a></li>',myPage,re.S)
        #汽车
        #先进行一次匹配，否则得到的有自己不想要的东西，得到一个列表，其实该列表长度为1，但我们仍然判断一下是否为空，然后for来循环一下,同时将for下面的缩进一下
        # itemdiv=re.findall(r'<div class="news_list">(.*?)</div>',myPage,re.S)
        # if itemdiv:
        #     for content in itemdiv:
        #         items=re.findall(r'\.shtml" target="_blank">(.*?)</a></li>',content,re.S)
        #         for item in items:
        #             #如果不encode的话，item是unicode格式，没法进行下面的去除字符串处理
        #             it=item.encode('utf-8')
        #             item1=self.replace_char(it)
        #             self.data.append(item1)
        #游戏
        # items=re.findall(r'\.html\' target="_blank">(.*?)</a>  <i>',myPage,re.S)
        #房产
        items=re.findall(r'\.html\' target=_blank>(.*?)</a> <i class="gray">',myPage,re.S)
        for item in items:
            #如果不encode的话，item是unicode格式，没法进行下面的去除字符串处理
            it=item.encode('utf-8')
            item1=self.replace_char(it)
            self.data.append(item1)
            print item1


if __name__=='__main__':
    index=1
    sp=zhongguowang_spider()
    # while index<=20:
        #足球
        # url=r'http://sports.china.com.cn/node_7118317_%d.htm' %index
        # url1='http://sports.china.com.cn/node_7118293_%d.htm' %index
        # sp.save_data(url)
        # sp.save_data(url1)
        # index+=1
    #健康
    #医药
    # url=r'http://health.china.com.cn/node_542850.htm'
    # sp.save_data(url)
    # url1='http://health.china.com.cn/node_542850_%d.htm' %index
    # while index<=3:
    #     sp.save_data(url1)
    #     index+=1
    #癌症
    # while index<=15:
    #     url=r'http://health.china.com.cn/node_542839_%d.htm' %index
    #     sp.save_data(url)
    #     index+=1
    #糖尿病
    # while index<=15:
    #     url=r'http://health.china.com.cn/node_542841_%d.htm' %index
    #     sp.save_data(url)
    #     index+=1
    #汽车
    # while index<=20:
    #     url=r'http://app.auto.china.com.cn/news/column.php?cname=资讯&p=%d' %index
    #     sp.save_data(url)
    #     index+=1
    #游戏
    # while index<=10:
    #     #手游
    #     # url=r'http://game.people.com.cn/GB/210053/index%d.html' %index
    #     #业界
    #     url=r'http://game.people.com.cn/GB/48662/index%d.html' %index
    #     sp.save_data(url)
    #     # sp.get_data(url)
    #     index+=1
    #房产
    while index<=5:
        #房产要闻 1-3页
        # url=r'http://house.people.com.cn/GB/194441/index%d.html' %index
        #各地楼市 1-4页
        # url=r'http://house.people.com.cn/GB/164305/index%d.html' %index
        #住房保障 1-4页
        # url=r'http://house.people.com.cn/GB/164315/index%d.html' %index
        #品牌房企 1-2页
        # url=r'http://house.people.com.cn/GB/164306/index%d.html' %index
        # sp.save_data(url)
        # # sp.get_data(url)
        # index+=1
        #人民出品 1-5页
        # url=r'http://house.people.com.cn/GB/164291/index%d.html' %index
        # sp.save_data(url)
        # # sp.get_data(url)
        # index+=1
        #政策宏观 1-4页
        url=r'http://house.people.com.cn/GB/167739/index%d.html' %index
        sp.save_data(url)
        # sp.get_data(url)
        index+=1