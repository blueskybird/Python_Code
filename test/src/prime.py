# -*- coding: utf-8 -*-
import math
import datetime

num=int(raw_input('input a num:'))

begin=datetime.datetime.now()

primelist=[1]*(num+1)
primenum=0

primelist[0]=0
primelist[1]=0

i=2

while i <= math.sqrt(num):
    j=i
    if primelist[i]:
        while j*i<=num:
            primelist[j*i]=0
            j+=1
    i+=1
    
i=2
n=len(primelist)
while i<n:
    if primelist[i]:
        primenum+=1
        print i
    i+=1

print '{a}以内的素数一共有：{b}'.format(a=num, b=primenum)

end=datetime.datetime.now()
print '一共用时：',end-begin