 #-*- coding: UTF-8 -*-
from time import ctime,sleep
import thread

'''
Python提供用于多线程编程的模块有thread，threading，Queue等，
thread和threading都允许程序员创建和管理线程，但thread提供基本线程和锁支持，
threading是比thread更高级的模块，功能更强。
ueue 模块允许用户创建一个可以用于多个线程之间共享数据的队列数据结构。

建议使用threading和Queue，不建议使用thread
'''

def loop0():
    print 'start loop 0 at:',ctime()
    sleep(4)
    print 'loop 0 done at:',ctime()

def loop1():
    print 'start loop 1 at:',ctime()
    sleep(2)
    print 'loop 1 done at:',ctime()

def main():
    print 'starting at:',ctime()
    # 这种方法是顺序执行，总时间是两个loop函数的和
    # loop0()
    # loop1()
    # 这种方法是多线程执行,导入thread模块，
    # 使用thread中的start_new_thread()方法，此处使用thread只是演示用,
    # thread的start_new_thread()方法一定前两个参数，一个函数名，一个函数所需的参数，
    # 由于我们的函数不需要参数，所以传一个空元组即可，
    # 同时需要加上sleep(6),因为如果不加的话，主线程没有使用锁，
    # 主线程会直接往下运行，执行print 'all DONE at:',ctime()此句，
    # 这样就退出了，使用sleep是为了让主线程等着子线程结束后再退出，也可以使用锁，就可以不用sleep了
    thread.start_new_thread(loop0,())
    thread.start_new_thread(loop1,())
    sleep(6)
    print 'all DONE at:',ctime()

if __name__=='__main__':
    main()