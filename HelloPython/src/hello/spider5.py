# -*- coding: utf-8 -*-
#coding:gbk

import re
#a=re.compile(r"""\d+   #the integral part
#                  \.   #the decimal point
#                  \d*  #some fractional digits"""  , re.X)
#
#b=re.compile(r"\d+\.\d*")
#
#match11=a.match('0.1415')
#match12=a.match('33')
#match21=a.match('3333.1415')
#match22=a.match('33')
#
#ab="bushi"
#if match11:
#    print match11.group()
#else:
#    print "dsa"
#if match12:
#    print match12.group()
#if match21:
#    print match21.group()
#if match22:
#    print match22.group()
my ='<mon="a=1&p=1&z=Bayen&pn=2" target="_blank">我是图片1</a>的就是垃圾<mon="a=1&p=1&z=Bayen&pn=2" target="_blank">我是图片2</a>'
myItems = re.findall(r'mon=".*?">(.*?)</a>',my)
for mon1 in myItems:
    print mon1
print myItems
print my

#coding:utf-8
#import re
#
#line = '<img src="/files/attachments/00138729035993893cc9f9690e042848b0f7e1816815a36000/0" alt="tupian">'
#listtup = re.findall(r'<img src="(.*?)" alt="(.*?)"',line)
#for src,alt in listtup:
#   print src
#   print alt
#print listtup