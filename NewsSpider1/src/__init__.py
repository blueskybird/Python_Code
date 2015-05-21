# -*- coding: utf-8 -*-

import urllib2
import urllib
import re
import chardet

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
    def __init__(self):
        self.datas = []
        self.titles = []
        # self.page=1
        self.myTool = HTML_Tool()
        print u'已经启动中国网爬虫，咔嚓咔嚓'

    def replace_char(self,item):
        item1=item
        p = re.compile('\d+|”|“| |:|：|\(|\)|-|/|（|）|\\\\|%|\?|\[|\]|\#|\&|\*|\{|\}|\||\.|\w|，|＂|＂|》|《|<|=|>|"|、|？|’|‘|!|;|·|•|\+|,|~|！|３|…')
        item1=re.sub(p,'',item1)
        return item1

    def start(self):
        page=2
        while page<30:
            nowPage='%d'%page
            print nowPage
            self.baidu_tieba(nowPage)
            page+=1
        print u'爬虫报告：文件已下载到本地并打包成txt文件'
        print u'程序已退出...'


    def baidu_tieba(self,nowPage):
        bdurl='http://tech.china.com/news/net/index_'+nowPage+'.html'  #中华网IT新闻标题
        # bdurl='http://183.60.177.212/fin/hgyw/index_'+nowPage+'.html'   #中华网经济新闻标题
        # bdurl='http://military.china.com/news2/index_'+nowPage+'.html'    #中华网军事新闻标题
        # bdurl='http://ent.china.com/music/nei/index_'+nowPage+'.html'    #中华网音乐新闻标题
        # bdurl='http://edu.china.com/new/edunews/index_'+nowPage+'.html'    #中华网教育新闻标题
        print "*****"+bdurl
        # 获取最终的数据
        self.save_data(bdurl, nowPage)


        # 用来存储楼主发布的内容

    def save_data(self, url, nowPage):
        # 加载页面数据到数组中  
        self.get_data(url)
        filePath='F:\\srcText\\zhonghuaNet\\IT\\'.encode('utf-8')#中华网IT新闻标题
        # filePath='F:\\srcText\\zhonghuaNet\\Economic\\'.encode('utf-8')#中华网经济新闻标题
        # filePath='F:\\srcText\\zhonghuaNet\\Military\\'.encode('utf-8')#中华网军事新闻标题
        # filePath='F:\\srcText\\zhonghuaNet\\Music\\'.encode('utf-8')#中华网音乐新闻标题
        # filePath='F:\\srcText\\zhonghuaNet\\Education\\'.encode('utf-8')#中华网教育新闻标题
        print '路径'+filePath
        # 打开本地文件
        page=1
        for item in self.datas:
            pageNum='%d'%page
            f = open(filePath + pageNum + '.txt', 'w+')
            f.writelines(item)
            f.close()
            page=page+1
        # print u'爬虫报告：文件已下载到本地并打包成txt文件'
        # print u'程序已退出...'
        # print u'请按任意键退出...'
        # raw_input()

    # 获取页面源码并将其存储到数组中  
    def get_data(self, url):
        # myPage = urllib2.urlopen(url).read().decode('utf-8')
        print "----"+url
        myPage = urllib.urlopen(url).read()
        myPage=myPage.decode('utf-8').encode('utf-8')
        # 将myPage中的html代码处理并存储到datas里面
        # self.deal_data(myPage.decode('gbk'))
        self.deal_data(myPage)

    # 将内容从页面代码中抠出来  
    def deal_data(self, myPage):
        myItems = re.findall(r'" alt="(.*?)" /></a></div>', myPage,re.S)#新华网IT标题获取标题正则
        # myItems = re.findall(r'</span><a title="(.*?)" target="_blank" href="', myPage,re.S)#新华网经济标题获取标题正则
        # myItems = re.findall(r" target='_blank' class='title_default'>(.*?)</a>&nbsp;", myPage,re.S)#新华网军事标题获取标题正则
        # myItems = re.findall(r"\" target='_blank' class='title_default'>(.*?)</a>&nbsp;", myPage,re.S)#新华网音乐标题获取标题正则
        # myItems = re.findall(r" target='_blank' class='title_default'>(.*?)</a>&nbsp;", myPage,re.S)#新华网教育标题获取标题正则
        for item in myItems:
            data = item.replace("\n", "").encode('utf-8')
            data=self.replace_char(item)
            self.datas.append(data + '\n')



# -------- 程序入口处 ------------------
print u"""#---------------------------------------
#   程序：中国网爬虫
#   版本：0.5 
#   作者：ls
#   日期：2013-05-16 
#   语言：Python 2.7 
#   操作：输入网址后自动只看楼主并保存到本地文件 
#   功能：将楼主发布的内容打包txt存储到本地。 
#--------------------------------------- 
"""


#伪装成浏览器访问网站
# bdurl='http://sports.baidu.com/n?cmd=1&class=worldsoccer&pn=1'
# nowPage='2'
# bdurl= 'http://military.china.com.cn/node_7207700_'+nowPage+'.htm'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# values = {'name': 'WHY',
#           'location': 'SDU',
#           'language': 'Python'}
# headers = {'User-Agent': user_agent}
# data = urllib.urlencode(values)
# req = urllib2.Request(bdurl, data, headers)

#调用
# mySpider = Baidu_Spider()
# mySpider.start()