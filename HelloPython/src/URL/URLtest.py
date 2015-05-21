#coding:utf-8

# from Class.Threadpool_Class import Threadpool_Class
import httplib

result_list=[]
black_list=[]

def testping(url):
    conn=httplib.HTTPConnection(url)
    conn.request("GET","/")
    r1=conn.getresponse()
    if r1.status==200:
        result_list.append(url)
        print "存在地址: %s " % url
    else:
        black_list.append(url)
        print "存在异常的地址: %s " % url

# obj=open('text.tasklist','r')
# t_obj=Threadpool_Class()
# for line in obj:
#     _domain=line.strip('\n')
#     if _domain.endswith('37.com'):
#         t_obj.execute(testping,_domain)
# obj.close()
# t_obj.dismiss(True)

print "一共有: %d 个地址正常访问,%d 个地址无法正常访问." % (len(result_list),len(black_list))

print "写入到结果文件中:web_access.text"
ac_result=open("web_access.text","w+")
for r_item in result_list:
    ac_result.write(r_item+"\n")
ac_result.close()

print "写入到结果文件中:web_error.text"
er_result=open("web_error.text","w+")
for r_item in black_list:
    er_result.write(r_item+"\n")
er_result.close()

print "Work Finish!!"