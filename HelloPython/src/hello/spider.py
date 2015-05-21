import urllib2

# url=r'http://d.weibo.com/100803?from=fangke#'
# url='http://www.baidu.com/'
url='http://ent.sina.com.cn/film/'
myPage = urllib2.urlopen(url).read().decode('gbk')
print myPage