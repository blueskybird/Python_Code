# -*- coding: utf-8 -*-


def Fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
#         result=Fib(n-1)+Fib(n-2)
#         return result
 
# print Fib(5) 
   
if __name__=='__main__':
    while True:
        inp=raw_input('input exit to quit,input a num to count :')
        if inp.lower()=='exit':
            print '结束！'
            exit()
        print Fib(int(inp))
#         