# -*- coding: utf-8 -*-

import urllib
import re

url=r'http://app.auto.china.com.cn/news/column.php?cname=资讯&p=2'

myPage=urllib.urlopen(url).read().decode('utf-8')

itemdiv=re.findall(r'<div class="news_list">(.*?)</div>',myPage,re.S)
it=itemdiv[0]
items=re.findall(r'\.shtml" target="_blank">(.*?)</a></li>',it,re.S)
for i in items:
    print i

print len(items)