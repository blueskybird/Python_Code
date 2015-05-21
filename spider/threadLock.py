#-*- coding: UTF-8 -*-

import thread
from time import ctime,sleep

'''这里不用像thread.py文件里那样需要在main函数中设置sleep（）函数，
使用锁可以使主线程在子线程结束后直接退出'''

loops=[4,2]

def loop(nloop,nsec,lock):
    print 'start loop',nloop,' at:',ctime()
    sleep(nsec)
    print 'loop',nloop,' done at:',ctime()
    lock.release()

def main():
    print 'starting at:',ctime()
    locks=[]
    nloops=range(len(loops))

    for i in nloops:
        lock=thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        thread.start_new_thread(loop,(i,loops[i],locks[i]))

    for i in nloops:
        while locks[i].locked():
            pass
    print 'all DONE at:',ctime()

if __name__=='__main__':
    main()