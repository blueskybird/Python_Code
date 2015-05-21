# -*- coding: utf-8 -*-

import urllib2
import urllib
import re

# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf-8')
# ----------- 处理页面上的各种标签 -----------


class HTML_Tool:
    # 用非 贪婪模式 匹配 \t 或者 \n 或者 空格 或者 超链接 或者 图片  
    BgnCharToNoneRex = re.compile("(\t|\n| |<a.*?>|<img.*?>)")

    # 用非 贪婪模式 匹配 任意<>标签  
    EndCharToNoneRex = re.compile("<.*?>")

    # 用非 贪婪模式 匹配 任意<p>标签  
    BgnPartRex = re.compile("<p.*?>")
    CharToNewLineRex = re.compile("(<br/>|</p>|<tr>|<div>|</div>)")
    CharToNextTabRex = re.compile("<td>")

    # 将一些html的符号实体转变为原始符号  
    replaceTab = [("<", "<"), (">", ">"), ("&", "&"), ("&", "\""), (" ", " ")]

    def Replace_Char(self, x):
        x = self.BgnCharToNoneRex.sub("", x)
        # x = self.BgnPartRex.sub("\n    ",x)
        # x = self.CharToNewLineRex.sub("\n",x)
        # x = self.CharToNextTabRex.sub("\t",x)
        # x = self.EndCharToNoneRex.sub("",x)

        for t in self.replaceTab:
            x = x.replace(t[0], t[1])
        return x


class Baidu_Spider:
    # 申明相关的属性  
    def __init__(self, url):
        self.myUrl = url
        self.datas = []
        self.titles = []
        self.myTool = HTML_Tool()
        print u'已经启动百度贴吧爬虫，咔嚓咔嚓'

        # 初始化加载页面并将其转码储存

    def baidu_tieba(self):
        # 读取页面的原始信息并将其从gbk转码  
        myPage = urllib2.urlopen(self.myUrl).read().decode("gbk")
        title = "NewsTitle"
        print u'文章名称：' + title
        # 获取最终的数据  
        self.save_data(self.myUrl, title)


        # 用来存储楼主发布的内容

    def save_data(self, url, title):
        # 加载页面数据到数组中  
        self.get_data(url)
        # 打开本地文件  
        f = open('F:\\' + title + '1.txt', 'w+')
        f.writelines(self.datas)
        f.close()
        f = open('F:\\test.txt', 'w+')
        f.writelines(self.titles)
        f.close()
        print u'爬虫报告：文件已下载到本地并打包成txt文件'
        print u'请按任意键退出...'
        raw_input();

    # 获取页面源码并将其存储到数组中  
    def get_data(self, url):
        myPage = urllib2.urlopen(url).read()
        f = open('原文1.txt', 'w+')
        f.writelines(myPage)
        f.close()
        # 将myPage中的html代码处理并存储到datas里面
        # self.deal_data(myPage.decode('gbk'))
        self.deal_data(myPage)

    # 将内容从页面代码中抠出来  
    def deal_data(self, myPage):
        # myItems = re.findall('alt=".*?">.*?<p>(.*?)</p><p>',myPage,re.S)
        # myItems = re.findall(r'<a href="(.*?)" mon="col=\d.*?" target="_blank">',myPage,re.S)
        myItems = re.findall(r'<li>            <a href="(.*?)" mon="col=\d&amp;a=\d&pn=\d" target="_blank">', myPage,
                             re.S)

        for item in myItems:
            data = item.replace("\n", "").encode('gbk')
            data = data.replace('" class="title" target="_blank', "")
            print "我是data:" + data
            content = urllib2.urlopen(data).read()
            textCode=re.findall(r'<meta http-equiv="Content-Type" content="text/html; charset=(.*?)" />',content,re.S)
            if(len(textCode)==0):
                textCode=re.findall(r'<meta http-equiv="content-type" content="text/html;charset=(.*?)">',content,re.S)
            if(len(textCode)==0):
                textCode=re.findall(r'<meta http-equiv="Content-Type" content="text/html; charset=(.*?)" >',content,re.S)
            if(len(textCode)>=1):
                txtCode=textCode[0]
                if(txtCode.lower()=='gb2312'):
                    txtCode='gbk'
                print txtCode
                print "我是url",data
                content=content.decode(txtCode)
            else:
                txtCode='gbk'
                print "我是url",data
                content=content.decode(txtCode)
            # print content
            ti = re.findall(r'<title>(.*?)</title>', content, re.S)
            tii = ti[0]
            print tii
            self.titles.append(tii + '\n')
            self.datas.append(data + '\n')

            # myItems = re.findall('mon=".*?" target="_blank">(.*?)</a>',myPage,re.S)
            # for item in myItems:
            # data = self.myTool.Replace_Char(item.replace("\n","").encode('gbk'))
            # self.datas.append(data+'\n')



# -------- 程序入口处 ------------------
print u"""#---------------------------------------
#   程序：百度贴吧爬虫 
#   版本：0.5 
#   作者：why 
#   日期：2013-05-16 
#   语言：Python 2.7 
#   操作：输入网址后自动只看楼主并保存到本地文件 
#   功能：将楼主发布的内容打包txt存储到本地。 
#--------------------------------------- 
"""


# print u'请输入贴吧的地址最后的数字串：'
#bdurl = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))
#bdurl = 'http://mil.sohu.com/'

#伪装成浏览器访问网站
# bdurl='http://sports.baidu.com/n?cmd=1&class=worldsoccer&pn=1'
bdurl = 'http://mil.news.baidu.com/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'name': 'WHY',
          'location': 'SDU',
          'language': 'Python'}
headers = {'User-Agent': user_agent}
data = urllib.urlencode(values)
req = urllib2.Request(bdurl, data, headers)

#调用
# mySpider = Baidu_Spider(bdurl)
mySpider = Baidu_Spider(req)
mySpider.baidu_tieba()