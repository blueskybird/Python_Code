import  urllib2


class JudgeLink():
    def __init__(self):
        pass
  
    def send_request(self,url):  
        try:
            res = urllib2.urlopen(urllib2.Request(url))  
            code = res.getcode()  
            res.close()  
            return code  
        except Exception,e:
            print e
            return 404

a=JudgeLink()
print a.send_request('http://www.baidu.com/')