# -*- coding: UTF-8 -*-
import datetime
# begintime=datetime.datetime.now()
# number=raw_input()
# num=1
# end=[]
# b=0
# n=0
# while num<int(number):
#     div=1
#     while div<num:
#         result=float(num)/div
#         if float(result).is_integer():
#             n+=1
#             if n>1:break
#         div+=1
#     if n==1:
#         end.append(num)
#     num+=1
#     n=0
# print "The prime number smaller then %s are:\n" % str(number)
# endtime=datetime.datetime.now()
# spendtime=endtime-begintime
# print "The calculate spend %s " % spendtime
# raw_input()

def prime(beginNum,number):
    begintime=datetime.datetime.now()
    num=beginNum
    n=0
    end=[]
    while num<int(number):
        div=1
        while div<num:
            # if (num!=2) and (float(num)/2).is_integer():
            #     break
            # elif (num!=3) and (float(num)/3).is_integer():
            #     break
            # elif (num!=5) and (float(num)/5).is_integer():
            #     break
            # elif (num!=7) and (float(num)/7).is_integer():
            #     break
            if num==2 or num==3 or num==5 or num==7:
                end.append(num)
                num+=1
            if num/2==0 or num/3==0 or num/5==0 or num/7==0:
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

print prime(900001,1000000)