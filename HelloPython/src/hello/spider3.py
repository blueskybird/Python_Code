#-*- coding: UTF-8 -*- 
from urllib2 import Request, urlopen, URLError, HTTPError

import urllib2

import re
from operator import itemgetter

#old_url='http://rrurl.cn/b1UZuP'
#req=Request(old_url)
#response=urlopen(req)
#print 'Old url :'+old_url
#print 'Real url :'+ response.geturl()

#old_url='http://www.baidu.com'
#req=Request(old_url)
#response=urlopen(req)
#print 'Info():'
#print response.info()

#request = urllib2.Request('http://www.baidu.com/')  
#request.add_header('User-Agent', 'fake-client')  
#response = urllib2.urlopen(request)  
#print response.read()

#my_url = 'http://www.google.cn'  
#response = urllib2.urlopen(my_url)  
#redirected = response.geturl() == my_url  
#print redirected  
#  
#my_url = 'http://rrurl.cn/b1UZuP'  
#response = urllib2.urlopen(my_url)  
#redirected = response.geturl() == my_url  
#print redirected

url='http://www.chinanews.com/gn/2015/01-10/6955433.shtml'
urldata=urllib2.urlopen(url).read()
ti= re.findall(r'<title>(.*?)</title>',urldata,re.S)
print ti
for i in ti:
    print i.decode('gbk')
da=r'<l>第一个。<p></p>第二个。<p></p>'
a=re.findall('(.*?)。<p></p>', da, re.S)
b=re.finditer('(.*?)。<p></p>', da, re.S)
print a
for j in a:
    print j.decode('utf-8')
print b
