# -*- coding: utf-8 -*-
  
import urllib2  
import re  
  
#------------------------------------------------------------------------------
def crawl(keyword_name):
    a = keyword_name

    # output.write(a+"\t")

    for year in range(2006,2013):
        for month in range(1,13):
            begintime=str(year)+"-"+"%02d"%month+"-01"
            endtime=str(year)+"-"+"%02d"%month+"-31"
            print begintime,endtime
            userMainUrl="http://search.sina.com.cn/?time=custom&stime="+begintime+"&etime="+endtime+"&c=news&q="+a+"&sort=time&range=title"
            print userMainUrl
            req = urllib2.Request(userMainUrl)
            resp = urllib2.urlopen(req)
            respHtml = resp.read()
            #print "respHtml=",respHtml # you should see the ouput html  

            urlpat = re.compile(r'<div class="l">(.*?)</div>')
            #<div class="l">我们为您搜索到2,005条新闻结果</div>
            print len(match)
            match = urlpat.findall(respHtml)
            for numstr in match:
                searchnum = numstr[14:-10]
                print "searchnum=",searchnum
                # output.write(searchnum+"\t")



    year=2013
    for month in range(1,3):
        begintime=str(year)+"-"+"%02d"%month+"-01"
        endtime=str(year)+"-"+"%02d"%month+"-31"
        print begintime,endtime
        userMainUrl="http://search.sina.com.cn/?time=custom&stime="+begintime+"&etime="+endtime+"&c=news&q="+a+"&sort=time&range=title"
        print userMainUrl
        req = urllib2.Request(userMainUrl)
        resp = urllib2.urlopen(req)
        respHtml = resp.read()
        #print "respHtml=",respHtml # you should see the ouput html

        match = urlpat.findall(respHtml)
        #<div class="l">我们为您搜索到2,005条新闻结果</div>
        urlpat = re.compile(r'<div class="l">(.*?)</div>')
        for numstr in match:
            searchnum = numstr[14:-10]
        print "searchnum=",searchnum
        # output.write(searchnum+"\t")

        # output.write("\r\n")


###############################################################################  
if __name__=="__main__":  
    # with open('input.txt', 'r') as fp:
    #     output = open('output.txt', 'a')
    #     for line in fp:
    #         keyword = line.strip()
    #         crawl(keyword)
        # output.close()

    crawl('用友软件')