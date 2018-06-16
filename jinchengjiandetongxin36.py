#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# 进程间的通信
# Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
# 我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据
import os, time, random
from multiprocessing import Process, Queue
# 向队列里面写入数据
def queue_write(queue):
    print('write process id is %s。parent process id is %s' % (os.getpid(), os.getppid()))

    for x in ['ass', 'www', '233']:
        queue.put(x)
        time.sleep(random.random())

# 从队列里面读取数据
def queue_read(queue):
    print('read process id is %s。parent process id is %s' % (os.getpid(), os.getppid()))

    while True:
        value = queue.get(True)
        print('Get %s from queue.' % value)




# # 父进程创建Queue
q = Queue()

pw = Process(target=queue_write, args=(q, )) # 创建子进程，同时绑定queue_write与队Queue对象
pr = Process(target=queue_read, args=(q, ))

pw.start()
pr.start()
pw.join() # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步


if q.empty():
    pr.terminate() # pr进程里是死循环，无法等待其结束，只能强行终止:

# 在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。