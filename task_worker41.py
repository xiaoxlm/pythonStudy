#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-


import time, sys, queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
# QueueManager.register('get_task_queue')
# QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行task_master.py的机器:
server_addr = '172.16.20.99'
print('connect to server %s...' % server_addr)

# 端口和验证码注意保持与task_master.py设置的完全一致:
manager = QueueManager(address = (server_addr, 5000), authkey=b'abc')
# 把两个Queue都注册到网络上，callable关联了Queue对象。 在这注册好理解一些
manager.register('get_task_queue')
manager.register('get_result_queue')

manager.connect()

# 获取Queue的对象:
task_queue = manager.get_task_queue()
result_queue = manager.get_result_queue()

for i in range(10):
    try:
        get = task_queue.get(timeout = 10)
        print('task_worker receive:', get)
        time.sleep(1)
        result_queue.put(get * get)
    except queue.Empty:
        print('task queue is empty.')

print('worker exit.')


