#coding:utf-8

import httplib
import re
import datetime

result_list=[]
blacksite_list=[]
blacksitepage_list=[]

def urlping(url):
    if url:#url非空
        # 去掉网址的http://，htp://等
        items=re.findall(r'://(.*)',url)
        # 如果是形如：www.tubestation.com.cn这样的站点，items将为空，所以判断下
        if len(items):#items不为空
            # 获取站点和该站点的网页
            its=re.findall(r'(.*?)/(.*)',items[0])
            site=its[0][0]
            # 网页地址前要加一个  /  线才行
            sitepage='/'+its[0][1]
        else:#items为空
            # 获取站点和该站点的网页
            its=re.findall(r'(.*?)/(.*)',url)#如果是形如www.tubestation.com.cn的网址，its也可能为空，如果是www.tubestation.com.cn/1245.html,its就不为空了
            if len(its):#its不为空
                site=its[0][0]
                # 网页地址前要加一个  /  线才行
                sitepage='/'+its[0][1]
            else:#its为空
                site=url
                sitepage='/'
        # 访问地址获取返回状态
        conn=httplib.HTTPConnection(site)
        try:
            conn.request('GET',sitepage)
        except:
            blacksite_list.append(url)
            print '无效的站点'
            print url
        else:
            sta=conn.getresponse().status
            print sta
            if sta<=307:
                result_list.append(url)
                print '有效的url'
            else:
                blacksitepage_list.append(url)
                print '无效的站点网页'

# 写到文件中
def output(filename,lists):
    # fileName='2014豆瓣电影.txt'.decode('utf-8')
    f=open('F:\\website\\'+filename,'w')
    for eachkey in lists:
        f.write(eachkey)
        f.write('\n')
    f.close()

def main():
    a=datetime.datetime.now()
    f=open(r'F:\website\webaddr.txt','r')
    lines=f.read()
    f.close()
    lines=lines.split('\n')
    print len(lines)
    for line in lines:
        urlping(line)
    output('result_list.txt',result_list)
    output('blacksite_list.txt',blacksite_list)
    output('blacksitepage_list.txt',blacksitepage_list)
    b=datetime.datetime.now()
    print (b-a).seconds

if __name__=='__main__':
    main()
