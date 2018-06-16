#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

# 总结一下就是，多任务的实现有3种方式：
#
# 多进程模式；
# 多线程模式；
# 多进程+多线程模式 (当然这种模型更复杂，实际很少采用。)

# 同时执行多个任务通常各个任务之间并不是没有关联的，而是需要相互通信和协调，有时，任务1必须暂停等待任务2完成后才能继续执行，有时，任务3和任务4又不能同时执行，所以，多进程和多线程的程序的复杂度要远远高于我们前面写的单进程单线程的程序。

# 因为复杂度高，调试困难，所以，不是迫不得已，我们也不想编写多任务。但是，有很多时候，没有多任务还真不行。想想在电脑上看电影，就必须由一个线程播放视频，另一个线程播放音频，否则，单线程实现的话就只能先把视频播放完再播放音频，或者先把音频播放完再播放视频，这显然是不行的。

# 线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程，完全由操作系统决定，程序自己不能决定什么时候执行，执行多长时间。

# 多进程和多线程的程序涉及到同步、数据共享的问题，编写起来更复杂。




# 多进程
# Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
# 子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。

# import os
#
# print('Process (pid:%s) start' % os.getpid())
#
# pid = os.fork()  # 在该进程上fork出一个子进程
#
# if pid == 0:
#     print("my pid is %s, my father pid is %s" % (os.getpid(), os.getppid())) # 调用getppid()就可以拿到父进程的ID。
#
# elif pid > 0:
#     print("my pid is %s, my child pid is %s" % (os.getpid(), pid))


# 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。




# multiprocessing
# 由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。
# ultiprocessing模块提供了一个Process类来代表一个进程对象
from multiprocessing import Process, Pool
import os, time, random
# 子进程要执行的代码
# def child_process(name):
#     print("run child process %s (%s)" % (name, os.getpid()))
#     print("my parent pid is (%s)" % (os.getppid()))
#
# #if __name__ == 'main':
# print('Parent process\'s pid is %s' % os.getpid())
# child_P = Process(target=child_process, args=('test',)) # 创建一个Process实例, 只需要传入一个执行函数和函数的参数, 相当于fork了一个进程，只是说Process被python封装过
# print('Child process will start.')
# child_P.start() # 用start()方法启动，这样创建进程比fork()还要简单
# child_P.join() # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
# print('Child process end.')





# Pool
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程
# 子进程要执行的代码
# def child_process(name):
#     start = time.time()
#     print('run task. my pid is %s, my parent pid is %s' % (os.getpid(), os.getppid()))
#     time.sleep(random.random()*3)  #random.random() 随机返回0.0到1.0之间的float数
#     end_time = time.time()
#     print('Task %s run %0.2f seconds' % (name, (end_time - start)))
#
#
# print('this process pid is %s' % os.getpid())
# p = Pool(4) # 最多同时执行4个进程
# for x in range(5):
#     child_name = 'subprocess' + str(x)
#     p.apply_async(child_process, args=(child_name, ))
#
# print('Waiting for all subprocesses done...')
# p.close() # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
# p.join() # 对Pool对象调用join()方法会等待所有子进程执行完毕
# print('All subprocesses done.')

# 由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。





# 子进程
# 很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
import subprocess
# 在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的
print('nslookup www.baidu.com')
r = subprocess.call(['nslookup', 'www.baidu.com'])
print('Exit code:', r)






