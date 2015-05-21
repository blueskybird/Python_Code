# -*- coding: utf-8 -*-

import urllib2
import cookielib
import WeiboEncode
import WeiboSearch
import WeiboGetData
import re

class WeiboLogin:
    def __init__(self, user, pwd, enableProxy = False):
        "初始化WeiboLogin，enableProxy表示是否使用代理服务器，默认关闭"
        print "Initializing WeiboLogin..."
        self.userName = user
        self.passWord = pwd
        self.enableProxy = enableProxy

        self.serverUrl = "http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.11)&_=1379834957683"
        self.loginUrl = "http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.11)"
        self.postHeader = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0'}


    def Login(self):
        "登陆程序"
        self.EnableCookie(self.enableProxy)#cookie或代理服务器配置

        serverTime, nonce, pubkey, rsakv = self.GetServerTime()#登陆的第一步
        postData = WeiboEncode.PostEncode(self.userName, self.passWord, serverTime, nonce, pubkey, rsakv)#加密用户和密码
        print "Post data length:\n", len(postData)
        req = urllib2.Request(self.loginUrl, postData, self.postHeader)
        print "Posting request..."
        result = urllib2.urlopen(req)#登陆的第二步——解析新浪微博的登录过程中3
        text = result.read()
        try:
            loginUrl = WeiboSearch.sRedirectData(text)#解析重定位结果
            urllib2.urlopen(loginUrl)
        except:
            print 'Login error!'
            return False

        print 'Login sucess!'
        return True


    def EnableCookie(self, enableProxy):
        '''
        Enable cookie & proxy (if needed).
        '''

        cookiejar = cookielib.LWPCookieJar()#建立cookie
        cookie_support = urllib2.HTTPCookieProcessor(cookiejar)
        if enableProxy:
            proxy_support = urllib2.ProxyHandler({'http':'http://xxxxx.pac'})#使用代理
            opener = urllib2.build_opener(proxy_support, cookie_support, urllib2.HTTPHandler)
            print "Proxy enabled"
        else:
            opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)#构建cookie对应的opener


    def GetServerTime(self):
        '''
        Get server time and nonce, which are used to encode the password
        '''

        print "Getting server time and nonce..."
        serverData = urllib2.urlopen(self.serverUrl).read()#得到网页内容
        print serverData
        try:
            serverTime, nonce, pubkey, rsakv = WeiboSearch.sServerData(serverData)#解析得到serverTime，nonce等
            return serverTime, nonce, pubkey, rsakv
        except:
            print 'Get server time & nonce error!'
            return None


class WeiboGet:
    def getdata(self,url):
        mypage = urllib2.urlopen(url).read().decode('utf-8')

        items_data = re.findall(r'node-type=\\"feed_list_content\\">(.*?)<', mypage, re.S)
        items_name = re.findall(r'nick-name=\\"(.*?)\\"', mypage, re.S)

        # return items_data,items_name
        for i in range(len(items_data)):
            print items_name[i],'**',items_data[i]

        print '--------------------------------------------------------------'

if __name__ == '__main__':
    weiboLogin = WeiboLogin('619434533@qq.com', 'Lishuai0321') #邮箱（账号）、密码
    if weiboLogin.Login() == True:
        print "登陆成功！"

    # weiboGet = WeiboGet()

    filenames = []

    filenames.append('sport')
    filenames.append('food')
    filenames.append('economic')
    filenames.append('tecnology')
    filenames.append('health')
    filenames.append('constellation')
    filenames.append('travel')

    for i in range(len(filenames)):
        #每次都重新创建是因为xinlangweibo_spider()在初始化时会创建全局变量self.data = []和self.name = []
        # 这样后面的url爬到数据就会重复添加，比如：food类的文本会包含sport文本。现在每次都重新创建就不会有此问题
        # 因为会重新初始化
        weiboGet = WeiboGetData.xinlangweibo_spider()
        # weiboGet = xinlangweibo_spider()
        index = 2
        url = ''
        filename = filenames[i]
        while index < 200:

            url_sport = r'http://d.weibo.com/102803_ctg1_1399_-_ctg1_1399?current_page=%d&since_id=&page=%d#feedtop' % ((index - 1)*3, index)
            url_food = r'http://d.weibo.com/102803_ctg1_2699_-_ctg1_2699?current_page=%d&since_id=&page=%d#feedtop' % ((index - 1)*3, index)
            url_economic = r'http://d.weibo.com/102803_ctg1_1299_-_ctg1_1299?current_page=%d&since_id=&page=%d#feedtop' % ((index - 1)*3, index)
            url_tecnology = r'http://d.weibo.com/102803_ctg1_2099_-_ctg1_2099?current_page=%d&since_id=&page=%d#feedtop' % ((index - 1)*3, index)
            url_health = r'http://d.weibo.com/102803_ctg1_2199_-_ctg1_2199?current_page=%d&since_id=&page=%d#feedtop' % ((index - 1)*3, index)
            url_constellation = r'http://d.weibo.com/102803_ctg1_1699_-_ctg1_1699?current_page=%d&since_id=&page=%d#feedtop' % ((index - 1)*3, index)
            url_travel = r'http://d.weibo.com/102803_ctg1_2599_-_ctg1_2599?current_page=%d&since_id=&page=%d#feedtop' % ((index - 1)*3, index)

            if i == 0:
                url = url_sport
            elif i == 1:
                url = url_food
            elif i == 2:
                url = url_economic
            elif i == 3:
                url = url_tecnology
            elif i == 4:
                url = url_health
            elif i == 5:
                url = url_constellation
            elif i == 6:
                url = url_travel

            # weiboGet.getdata(url)
            print url
            weiboGet.get_data(url)
            index += 1
        weiboGet.save_data(url, filename)