# -*- coding: UTF-8 -*-
import datetime
import threading
import time

b=0

class myThread (threading.Thread):
    def __init__(self, name,beginNum, number):
        threading.Thread.__init__(self)
        self.name = name
        self.beginNum=beginNum
        self.number = number
    def run(self):
        print "Starting " + self.name
       # 获得锁，成功获得锁定后返回True
       # 可选的timeout参数不填时将一直阻塞直到获得锁定
       # 否则超时后将返回False
        threadLock.acquire()
        primes.append(sum(prime(self.beginNum,self.number)))
        # 释放锁
        threadLock.release()

def prime(beginNum,number):
    begintime=datetime.datetime.now()
    num=beginNum
    n=0
    end=[]
    while num<int(number):
        div=1
        while div<num:
            #下面的方法效率更高
            # if (num!=2) and (float(num)/2).is_integer():
            #     break
            # elif (num!=3) and (float(num)/3).is_integer():
            #     break
            # elif (num!=5) and (float(num)/5).is_integer():
            #     break
            # elif (num!=7) and (float(num)/7).is_integer():
            #     break

            #此法效率更高
            if num==2 or num==3 or num==5 or num==7 or num==11 or num==13:
                end.append(num)
                num+=1
            if num%2==0 or num%3==0 or num%5==0 or num%7==0 or num%11==0 or num%13==0:
                break

            result=float(num)/div
            if float(result).is_integer():
                n+=1
                if n>1:break
            div+=1
        if n==1:
            end.append(num)
        num+=1
        n=0
    print beginNum,number
    endtime=datetime.datetime.now()
    spendtime=endtime-begintime
    print "The calculate spend %s " % spendtime
    return end

def sum(primes):
    summ=0
    for i in primes:
        summ+=i
    return summ

threadLock = threading.Lock()
threads = []
primes=[]

inputNum=raw_input('范围内:')
times=raw_input('线程数:')
numInteger=int(inputNum)
timesInteger=int(times)
for i in range(timesInteger):
    # 创建新线程
    if i==0:
        name='thread%s' %i
        name=myThread(i,1,numInteger/timesInteger)
    elif i==9:
        name='thread%s' %i
        name=myThread(i,numInteger/timesInteger * i+1,numInteger)
    else:
        name='thread%s' %i
        name=myThread(i,numInteger/timesInteger * i+1,numInteger/timesInteger * (i+1))


    # 开启新线程
    name.start()

    # 添加线程到线程列表
    threads.append(name)

# # 创建新线程
# thread1 = myThread(1, 1,numInteger/2)
# thread2 = myThread(2,numInteger-numInteger/2, numInteger)
#
# # 开启新线程
# thread1.start()
# thread2.start()
#
# # 添加线程到线程列表
# threads.append(thread1)
# threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()

print primes
print "Exiting Main Thread"
