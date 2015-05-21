# -*- coding: utf-8 -*-  
#一个简单的re实例，匹配字符串中的hello字符串  
  
#导入re模块  
#import re  
   
## 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”  
#pattern = re.compile(r'hello')  
#   
## 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None  
#match1 = pattern.match('hello world!')  
#match2 = pattern.match('helloo world!')  
#match3 = pattern.match('helllo world!')  
#match4 = pattern.search('hello world!')
#
#print "第一个"+match4.group()  
#print pattern.split('hihellonihao')
#print pattern.split('hihellonihao')[0]
#print pattern.findall('hihellonihao')
#
##如果match1匹配成功  
#if match1:  
#    # 使用Match获得分组信息  
#    print match1.group()  
#else:  
#    print 'match1匹配失败！'  
#  
#  
##如果match2匹配成功  
#if match2:  
#    # 使用Match获得分组信息  
#    print match2.group()  
#else:  
#    print 'match2匹配失败！'  
#  
#  
##如果match3匹配成功  
#if match3:  
#    # 使用Match获得分组信息  
#    print match3.group()  
#else:  
#    print 'match3匹配失败！'  

import re  
   
p = re.compile(r'(\w+) (\w+)')  
s = 'i say, hello world!'  
   
print p.sub(r'\2 \1', s)  
   
def func(m):  
    return m.group(1).title() + ' ' + m.group(2).title()  
   
print p.sub(func, s)
#import re  
#   
#p = re.compile(r'\d+')  
#print p.findall('one12two2three3four4')  
