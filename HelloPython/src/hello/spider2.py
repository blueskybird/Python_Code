# -*- coding: utf-8 -*-  
#---------------------------------------  
#   ���򣺰ٶ��������  
#   �汾��0.5  
#   ���ߣ�why  
#   ���ڣ�2013-05-16  
#   ���ԣ�Python 2.7  
#   ������������ַ���Զ�ֻ��¥�������浽�����ļ�  
#   ���ܣ���¥�����������ݴ��txt�洢�����ء�  
#---------------------------------------  
   
import string  
import urllib2  
import re  
  
#----------- ����ҳ���ϵĸ��ֱ�ǩ -----------  
class HTML_Tool:  
    # �÷� ̰��ģʽ ƥ�� \t ���� \n ���� �ո� ���� ������ ���� ͼƬ  
    BgnCharToNoneRex = re.compile("(\t|\n| |<a.*?>|<img.*?>)")  
      
    # �÷� ̰��ģʽ ƥ�� ����<>��ǩ  
    EndCharToNoneRex = re.compile("<.*?>")  
  
    # �÷� ̰��ģʽ ƥ�� ����<p>��ǩ  
    BgnPartRex = re.compile("<p.*?>")  
    CharToNewLineRex = re.compile("(<br/>|</p>|<tr>|<div>|</div>)")  
    CharToNextTabRex = re.compile("<td>")  
  
    # ��һЩhtml�ķ��ʵ��ת��Ϊԭʼ���  
    replaceTab = [("<","<"),(">",">"),("&","&"),("&","\""),(" "," ")]  
      
    def Replace_Char(self,x):  
        x = self.BgnCharToNoneRex.sub("",x)  
        x = self.BgnPartRex.sub("\n    ",x)  
        x = self.CharToNewLineRex.sub("\n",x)  
        x = self.CharToNextTabRex.sub("\t",x)  
        x = self.EndCharToNoneRex.sub("",x)  
  
        for t in self.replaceTab:    
            x = x.replace(t[0],t[1])    
        return x    
      
class Baidu_Spider:  
    # ������ص�����  
    def __init__(self,url):    
        self.myUrl = url + '?see_lz=1'  
        self.datas = []  
        self.myTool = HTML_Tool()  
        print u'已经启动百度贴吧爬虫，咔嚓咔嚓'  
    
    # ��ʼ������ҳ�沢����ת�봢��  
    def baidu_tieba(self):  
        # ��ȡҳ���ԭʼ��Ϣ�������gbkת��  
#        myPage = urllib2.urlopen(self.myUrl).read().decode("gbk")
        myPage = urllib2.urlopen(self.myUrl).read().decode("utf-8")  
        # ����¥����������һ���ж���ҳ  
        endPage = self.page_counter(myPage)  
        # ��ȡ����ı���  
        title = self.find_title(myPage)  
        print u'文章名字' + title  
        # ��ȡ���յ����  
        self.save_data(self.myUrl,title,endPage)  
  
    #��������һ���ж���ҳ  
    def page_counter(self,myPage):  
        # ƥ�� "����<span class="red">12</span>ҳ" ����ȡһ���ж���ҳ  
        myMatch = re.search(r'class="red">(\d+?)</span>', myPage, re.S)  
        if myMatch:    
            endPage = int(myMatch.group(1))  
            print u'爬虫报告：发现楼主共有%d页的原创内容' % endPage  
        else:  
            endPage = 0  
            print u'爬虫报告：无法计算楼主发布内容有多少页！'  
        return endPage  
  
    # ����Ѱ�Ҹ���ı���  
    def find_title(self,myPage):  
        # ƥ�� <h1 class="core_title_txt" title="">xxxxxxxxxx</h1> �ҳ�����  
        myMatch = re.search(r'<h1.*?>(.*?)</h1>', myPage, re.S)  
        title = u'暂无标题'  
        if myMatch:  
            title  = myMatch.group(1)  
        else:  
            print u'爬虫报告：无法加载文章标题！'  
        # �ļ����ܰ������ַ� \ / �� * ? " < > |  
        title = title.replace('\\','').replace('/','').replace(':','').replace('*','').replace('?','').replace('"','').replace('>','').replace('<','').replace('|','')  
        return title  
  
  
    # �����洢¥������������  
    def save_data(self,url,title,endPage):  
        # ����ҳ����ݵ�������  
        self.get_data(url,endPage)  
        # �򿪱����ļ�  
        f = open(title+'.txt','w+')  
        f.writelines(self.datas)  
        f.close()  
        print u'爬虫报告：文件已下载到本地并打包成txt文件'   
        print u'请按任意键退出...'
        raw_input();  
  
    # ��ȡҳ��Դ�벢����洢��������  
    def get_data(self,url,endPage):  
        url = url + '&pn='  
        for i in range(1,endPage+1):  
            print u'爬虫报告：爬虫%d号正在加载中...' % i 
            myPage = urllib2.urlopen(url + str(i)).read()  
            # ��myPage�е�html���봦�?�洢��datas����  
            self.deal_data(myPage.decode('utf-8'))  
              
  
    # �����ݴ�ҳ������пٳ���  
    def deal_data(self,myPage):  
        myItems = re.findall('id="post_content.*?>(.*?)</div>',myPage,re.S)  
        for item in myItems:  
            data = self.myTool.Replace_Char(item.replace("\n","").encode('utf-8'))  
            self.datas.append(data+'\n')  
  
  
  
#-------- ������ڴ� ------------------  
print u"""#--------------------------------------- 
#   ���򣺰ٶ�������� 
#   �汾��0.5 
#   ���ߣ�why 
#   ���ڣ�2013-05-16 
#   ���ԣ�Python 2.7 
#   ������������ַ���Զ�ֻ��¥�������浽�����ļ� 
#   ���ܣ���¥�����������ݴ��txt�洢�����ء� 
#--------------------------------------- 
"""  
  
# ��ĳС˵���Ϊ����  
#bdurl = 'http://tieba.baidu.com/p/2296712428?see_lz=1&pn=1'  
bdurl='http://tieba.baidu.com/p/3381334878'  
print u'请输入贴吧的地址最后的数字串：'  
#bdurl = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))   
  
#����  
mySpider = Baidu_Spider(bdurl)  
mySpider.baidu_tieba() 
