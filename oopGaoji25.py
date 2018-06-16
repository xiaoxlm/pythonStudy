#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

# 定制类1
# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
# __slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。
# 除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。


# __str__
class Student(object):
    def __init__(self, name):
        self.name = name

print(Student('Michael'))
#<__main__.Student object at 0x109afb190> 打印出一堆<__main__.Student object at 0x109afb190>，不好看。

# 怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name

print(Student('Michaelxxx'))
# Student object (name: Michael)

# 但是细心的朋友会发现直接敲变量不用print，打印出来的实例还是不好看：
# s = Student('Michael')
# print(s)
# <__main__.Student object at 0x109afb310>  其实python3.5后不会出现这种情况

# 这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

# 解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return 'Student object (name=%s)' % self.name
#     __repr__ = __str__ # 偷懒的写法
#
# s = Student('Michael')
# print(s)



# __iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self): # 实例本身就是迭代对象，故返回自己
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b

        if self.a > 100:
            raise StopIteration(); # 退出循环的条件

        return self.a # 返回下一个值

for n in Fib():
    print(n)



# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：

def _getitem(self, n):
    a, b = 1, 1
    for x in range(n):
        a, b = b, a + b
    return a
Fib.__getitem__ = _getitem

print('\n', Fib()[2])

# list有个神奇的切片方法 list(range(100))[5:10]

# 对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
def _getitem2(self, n):
    if isinstance(n, int): # n是索引
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

    elif isinstance(n, slice):  # n是切片
        start = n.start
        stop = n.stop
        if start is None:
            start = 0

        a, b = 1, 1
        L = []
        for x in range(stop):
            if x >= start:
                L.append(a)
            a, b = b, a+b
        return L

Fib.__getitem__ = _getitem2
print('\n', Fib()[1:6])

# 完成上面的切片功能
def _fib(self, n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a + b
        self.L.append(a)
    return self.L

Fib.L = []
Fib.fib_list = _fib

print(Fib().fib_list(10)[2:4])
