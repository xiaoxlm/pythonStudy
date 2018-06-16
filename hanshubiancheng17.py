#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 装饰器
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。


# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# log相当于一个装饰器
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log   # 把@log放到now()函数的定义处，相当于执行了语句 now = log(now), 但@log必须放在函数前面！
def now():
    print('2016-10-11\n')
now()

# 套三层
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute') # 3层嵌套的效果是这样的 now = log('execute')(now)
def now():
    print('2016-10-11')

now()
print(now.__name__, '\n') # wrapper 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute') # 3层嵌套的效果是这样的 now = log('execute')(now)
def now():
    print('2016-10-11')

now()
print(now.__name__, '\n')

