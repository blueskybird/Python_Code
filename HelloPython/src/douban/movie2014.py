# -*- coding: utf-8 -*-

import urllib2
import re


class doubanmove:
    # 存放页面的url，存放每个页面中每个电影的url
    pageUrl=[]
    moveUrl=[]
    # 存放电影名字及评分
    moveNameAndRate={}

    # 按评分顺序存放电影名字
    sortMoveName=[]

    #获取豆瓣电影的分页的页面
    def PagesUrl(self,url,begin,end):
        for i in range(begin,end+1):
            #打开文件对象
            print url + str((i-1)*20)
            self.pageUrl.append(url + str((i-1)*20))

    # 获取每个电影的url
    def moviesUrl(self,pageUrl):
        for eachPage in pageUrl:
            page=urllib2.urlopen(eachPage).read()
            moviesItems=re.findall(r'<a class="nbg" href="(.*?)"  title="',page,re.S)
            for movieItem in moviesItems:
                self.moveUrl.append(movieItem)

    # 获取电影名字及评分
    def getMoveAndRate(self,moveUrl):
        for eachUrl in moveUrl:
            page=urllib2.urlopen(eachUrl).read()
            name=re.findall('<span property="v:itemreviewed">(.*?)</span>',page,re.S)
            rate=re.findall('<strong class="ll rating_num" property="v:average">(.*?)</strong>',page,re.S)
            if rate[0]:
                self.moveNameAndRate[name[0]]=rate[0]
        # 将得到的名字和评分按照评分从高到低排序,self.sortMoveName中存放的是按照评分从高到低排列后的名字顺序
        items=self.moveNameAndRate.items()
        backitems=[[v[1],v[0]] for v in items]
        backitems.sort(reverse=True)
        self.sortMoveName= [backitems[i][1] for i in range(0,len(backitems))]

    # 顺序执行上面的函数
    def run(self,url,begin,end):
        self.PagesUrl(url,begin,end)
        self.moviesUrl(self.pageUrl)
        self.getMoveAndRate(self.moveUrl)
        self.output(self.sortMoveName)

    # 写到文件中
    def output(self,sortMoveName):
        fileName='2014豆瓣电影.txt'.decode('utf-8')
        f=open('F:\\douban\\'+fileName,'w')
        for eachkey in sortMoveName:
            item=eachkey+'---'+self.moveNameAndRate[eachkey]
            f.write(item)
            f.write('\n')
        f.close()


if __name__ == '__main__':
    url='http://movie.douban.com/tag/2014%20电影?start='
    urll='http://movie.douban.com/tag/%E5%8A%A8%E7%94%BB?start=20&type=T'
    begin = input('请输入你抓取的页数开始为:')
    end = input('请输入你抓取的页数结束为:')
    move=doubanmove()
    move.run(url,begin,end)
