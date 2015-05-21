# -*- coding: utf-8 -*-

import urllib2
import urllib
import sys
import chardet
from bs4 import BeautifulSoup

nowPage='1'
bdurl='http://tech.china.com/news/net/index_'+nowPage+'.html'
print bdurl
myPage=urllib.urlopen(bdurl).read()
print myPage.encode('utf-8')
filePath='F:\\zhonghuaNet\\IT\\'.encode('utf-8')
# 打开本地文件
page='1'
f = open(filePath + page + '.txt', 'w+')
f.writelines(myPage)
f.close()