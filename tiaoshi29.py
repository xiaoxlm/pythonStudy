#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

# 断言
# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero'  # 这句话的意思是， n不应该=0， 如果等于0则断言失败，assert语句本身就会抛出AssertionError，同时提示后面的话
#     print(123)
#     return 10 / n
# foo(0)

# 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert

# python3 -O err.py

# 关闭后，你可以把所有的assert语句当成pass来看。




# logging
# import logging
#
#
# s = 0
# logging.basicConfig(level=logging.INFO, # 有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。
#                     format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='./test.log',
#                     filemode='w'
#                     )
# logging.info('n = %d' % s)




# pdb
# 启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序：
#
# # err.py
# s = '0'
# n = int(s)
# print(10 / n)
# 然后启动：
#
# $ python3 -m pdb err.py
# > /Users/michael/Github/learn-python3/samples/debug/err.py(2)<module>()
# -> s = '0'
# 以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。输入命令l来查看代码：
#
# (Pdb) l
#   1     # err.py
#   2  -> s = '0'
#   3     n = int(s)
#   4     print(10 / n)
# 输入命令n可以单步执行代码：
#
# (Pdb) n
# > /Users/michael/Github/learn-python3/samples/debug/err.py(3)<module>()
# -> n = int(s)
# (Pdb) n
# > /Users/michael/Github/learn-python3/samples/debug/err.py(4)<module>()
# -> print(10 / n)
# 任何时候都可以输入命令p 变量名来查看变量：
#
# (Pdb) p s
# '0'
# (Pdb) p n
# 0
# 输入命令q结束调试，退出程序：
#
# (Pdb) q
# 这种通过pdb在命令行调试的方法理论上是万能的，但实在是太麻烦了，如果有一千行代码，要运行到第999行得敲多少命令啊。还好，我们还有另一种调试方法。





# pdb.set_trace()
# 这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点
import pdb
s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)

# 行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行：
# 这个方式比直接启动pdb单步调试效率要高很多，但也高不到哪去。
# 虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器。