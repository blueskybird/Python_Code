# -*- coding: utf-8 -*-

import urllib2
import urllib
import re

def replace_char(item):
        item=item.replace('”','')
        item=item.replace('“','')
        item=item.replace(' ','')
        item=item.replace(':','')
        item=item.replace('：','')
        return item

nowPage='23'
bdurl='http://edu.china.com/new/edunews/index_'+nowPage+'.html'
print bdurl
myPage=urllib.urlopen(bdurl).read().encode('utf-8')
# print myPage.decode('gbk')
# print myPage.encode('utf-8')
# print myPage
myItems = re.findall(r" target='_blank' class='title_default'>(.*?)</a>&nbsp;",myPage,re.S)
for item in myItems:
    item1=item.encode('utf-8')
    # item1=item1.replace('”','')
    # item1=item1.replace('“','')
    # item1=item1.replace(' ','')
    # item1=item1.replace(':','')
    # item1=item1.replace('：','')
    print '---'+item1+'---'
    # item11=replace_char(item1)
    print replace_char(item1)
    print '*******************************************************************************'
filePath='F:\\zhonghuaNet\\'.encode('utf-8')

# 打开本地文件
page='1'
f = open(filePath + page + '.txt', 'w+')
f.writelines(myPage)
f.close()
