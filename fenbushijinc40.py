#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

# 分布式进程
# 在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。

# Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。由于managers模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。

# 举个例子：如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，现在，由于处理任务的进程任务繁重，希望把发送任务的进程和处理任务的进程分布到两台机器上。怎么用分布式进程实现？

# 原有的Queue可以继续使用，但是，通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了。

# 我们先看服务进程，服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务：

# task_master

import time, random, queue
from multiprocessing.managers import BaseManager

# 初始化两个队列
# master发送任务的队列
task_queue = queue.Queue()
# master接收结果的队列
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass


# QueueManager.register('get_task_queue', callable = lambda: task_queue)
# QueueManager.register('get_result_queue', callable = lambda: result_queue)

# 绑定端口5000，设置验证码abc
manager = QueueManager(address = ('172.16.20.99', 5000), authkey = b'abc')
# 把两个Queue都注册到网络上，callable关联了Queue对象。 在这注册好理解一些
manager.register('get_task_queue', callable = lambda: task_queue)
manager.register('get_result_queue', callable = lambda: result_queue)

# 启动Queue
manager.start()

# 通过网络获取Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 请注意，当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，但是，在分布式多进程环境下，添加任务到Queue不可以直接对原始的task_queue进行操作，那样就绕过了QueueManager的封装，必须通过manager.get_task_queue()获得的Queue接口添加。

# 发送消息到任务
for x in range(10):
    # 随机生成0到10000的数据
    n = random.randint(0, 10000)
    task.put(n)
    print('put task %d...' % n)

print('try to get result...')
# 从队列获取消息
for i in range(10):
    r = result.get(timeout = 10) # 我的理解是 result.get()会一直挂着(挂10秒)，有数据写入队列后才返回数据，如果10秒内没有数据写入队列，就会报错。可以不给timeout参数，表示一直挂着没有时间限制
    print('get result %s...' % r)

manager.shutdown()
print('master exit.')


# 而Queue之所以能通过网络访问，就是通过QueueManager实现的。由于QueueManager管理的不止一个Queue，所以，要给每个Queue的网络调用接口起个名字，比如get_task_queue。
#
# authkey有什么用？这是为了保证两台机器正常通信，不被其他机器恶意干扰。如果task_worker.py的authkey和task_master.py的authkey不一致，肯定连接不上。
#
# 小结
#
# Python的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多台机器的环境下。
#
# 注意Queue的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。比如发送一个处理日志文件的任务，就不要发送几百兆的日志文件本身，而是发送日志文件存放的完整路径，由Worker进程再去共享的磁盘上读取文件。

