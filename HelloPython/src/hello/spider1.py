# -*- coding: utf-8 -*-  
#---------------------------------------  
#   �����ܰ�����  
#   �汾��0.2  
#   ���ߣ�why  
#   ���ڣ�2013-05-15  
#   ���ԣ�Python 2.7  
#   ����������quit�˳��Ķ����°ٿ�  
#   ���ܣ����»س�����������յ��ܰ��ȵ�  
#   ���£������������ʾ�������������  
#---------------------------------------  
   
import urllib2  
import urllib  
import re  
import thread  
import time  
  
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
#----------- ����ҳ���ϵĸ��ֱ�ǩ -----------  
  
  
#----------- ���ش������°ٿ� -----------  
class HTML_Model:  
      
    def __init__(self):  
        self.page = 1  
        self.pages = []  
        self.myTool = HTML_Tool()  
        self.enable = False  
  
    # �����еĶ��Ӷ��۳�������ӵ��б��в��ҷ����б�  
    def GetPage(self,page):  
#        myUrl = "http://m.qiushibaike.com/hot/page/" + page
        myUrl="http://www.qiushibaike.com/hot/page/2?s="
        myResponse  = urllib2.urlopen(myUrl)  
        myPage = myResponse.read()  
        #encode�������ǽ�unicode����ת�������������ַ�  
        #decode�������ǽ����������ַ�ת����unicode����  
        unicodePage = myPage.decode("utf-8")  
  
        # �ҳ�����class="content"��div���  
        #re.S������ƥ��ģʽ��Ҳ����.����ƥ�任�з�  
        myItems = re.findall('<div.*?class="content".*?title="(.*?)">(.*?)</div>',unicodePage,re.S)  
        items = []  
        for item in myItems:  
            # item �е�һ����div�ı��⣬Ҳ����ʱ��  
            # item �еڶ�����div�����ݣ�Ҳ��������  
            items.append([item[0].replace("\n",""),item[1].replace("\n","")])  
        return items  
  
    # ���ڼ����µĶ���  
    def LoadPage(self):  
        # ����û�δ����quit��һֱ����  
        while self.enable:  
            # ���pages�����е�����С��2��  
            if len(self.pages) < 2:  
                try:  
                    # ��ȡ�µ�ҳ���еĶ�����  
                    myPage = self.GetPage(str(self.page))  
                    self.page += 1  
                    self.pages.append(myPage)  
                except:  
                    print '无法连接糗事百科！'  
            else:  
                time.sleep(1)  
          
    def ShowPage(self,q,page):  
        for items in q:  
            print u'第%d页' % page , items[0]  
            print self.myTool.Replace_Char(items[1])  
            myInput = raw_input()  
            if myInput == "quit":  
                self.enable = False  
                break  
          
    def Start(self):  
        self.enable = True  
        page = self.page  
  
        print u'正在加载中......'  
          
        # �½�һ���߳��ں�̨���ض��Ӳ��洢  
        thread.start_new_thread(self.LoadPage,())  
          
        #----------- ���ش������°ٿ� -----------  
        while self.enable:  
            # ���self��page�����д���Ԫ��  
            if self.pages:  
                nowPage = self.pages[0]  
                del self.pages[0]  
                self.ShowPage(nowPage,page)  
                page += 1  
  
  
#----------- �������ڴ� -----------  
print u""" 
--------------------------------------- 
   �����ܰ����� 
   �汾��0.1 
   ���ߣ�why 
   ���ڣ�2013-05-15 
   ���ԣ�Python 2.7 
   ����������quit�˳��Ķ����°ٿ� 
   ���ܣ����»س�����������յ��ܰ��ȵ� 
--------------------------------------- 
"""  
  
  
print u'请按回车浏览今日的糗百内容'  
raw_input(' ')  
myModel = HTML_Model()  
myModel.Start()