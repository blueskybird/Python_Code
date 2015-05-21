# -*- coding: utf-8 -*-

import urllib2

#获取豆瓣读书的分页的页面
def doubanbook(url,begin,end):
    for i in range(begin,end+1):
        filename = str(i) + '.html'
        print 'Downloading ' + str(i) + '....... Filename is ' + filename
        #打开文件对象
        f = open('F:\\douban\\'+filename,'w+')
        print url + str((i-1)*20)
        m = urllib2.urlopen(url + str((i-1)*20)).read()
        f.write(m)
        f.close()

if __name__ == '__main__':
    url = 'http://book.douban.com/tag/计算机?start='
    begin = input('请输入你抓取的页数开始为:')
    end = input('请输入你抓取的页数结束为:')
    doubanbook(url,begin,end)
