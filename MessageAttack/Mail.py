#coding:utf-8

import smtplib
import sys
from email.mime.text import MIMEText

def sendMail(mail_to):
    mail_server = 'smtp.163.com'
    mail_port = '25'
    username = 'lishuai_gy@163.com'
    password = 'Lishuai'
    mail_title = 'python Test'
    mail_content = 'This is a test from python for sending email'
    if type(mail_to) == str:#之所以要有这样的判断是为了收件人是多个人或者传入的的收件人列表是以list的方式
        mail_list = mail_to.split(';') #将str类型的数据转换为list
    elif type(mail_to) == list:
        mail_list = mail_to
    else:
        print "你输入的收件人格式有误"

    try:
        handle = smtplib.SMTP(mail_server,mail_port)
        handle.login(username,password)
        # msg = "From:%srn To:%srnContent-Type: text/html;charset=gb2312rn Subject:%srnrn %s"%("杨彦星",";".join(mail_list),mail_title,mail_content) #这里的msg其实就是一种固定的格式，From:To:Subject
        content='hahaha,woshisheia!'
        msg=MIMEText(content)#content是正文内容
        msg['Subject']='nihao'#这句表示标题是什么
        # msg['From']=username
        msg['From']='619434533@qq.com'#这句显示发件人是谁，和实际由谁发不一样，handle.login(username,password)这个才是真正登陆发短信的人
        msg['To']=mail_to #这句显示是谁发来的
        handle.sendmail(username,mail_list,msg.as_string())
        # handle.sendmail(username,mail_to,msg.as_string())
        print "Send email sucess"
    except Exception,e:
        print "Send email failed because %s" % e

if __name__ =="__main__":
    sendMail('lishuai_gy@163.com;619434533@qq.com')