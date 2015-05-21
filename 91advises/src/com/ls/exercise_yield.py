#-*- coding: utf-8 -*-

from itertools import islice

def fib():
    a, b = 0, 1
#    for i in range(3):
    for i in range(5):
#    while True:
        yield a
        a, b = b, a+b
    print 'hello'
    

print list(islice(fib(), 5))


'''
当使用 for i in range(3)时，因为fib()函数只迭代3次，不按照islice(fib(), 5)里面的5进行迭代，所以结果是:

hello
[0, 1, 1]
之所以会打印 hello就是因为里面的循环结束了

当使用 for i in range(5)时，因为fib()函数迭代5次，而islice(fib(), 5)也迭代5次，yield返回值后连 a, b = b, a+b语句都没有执行， 所以结果是:

[0, 1, 1, 2, 3]
之所以不会打印 hello就是因为里面的循环到第五次时结束了

当使用while True时，按照islice(fib(), 5)里面的5进行迭代，所以结果是:

[0, 1, 1, 2, 3]
之所以不会打印 hello就是因为里面的循环不会结束
'''