#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

# 定制类2

# __getattr__ 有点类似于PHP里面的__get()魔术方法

class Student(object):

    def __init__(self):
        self.name = 'Michael'
        self.age = 18
        self.score = 0

    def __getattr__(self, item):  # 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值。
        if item == 'score':
            self.score = 99
            return self.score
        elif item == 'info':
            return lambda : 'name: %s, age: %d, score: %d' % (self.name, self.age, self.score)
        else:
            raise AttributeError('\'Student\' object has no attribute \'%s\'' % (item))


print(Student().score)
print(Student().info())
# print(Student().yoyo())
# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。

print('\n')
# __call__ 类似于PHP里面的__call()
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
#任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
class MyCall(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        print("My name is %s." % self.name)



my = MyCall('yoyo')
my(*('aa', 80), **{'ss':88})
# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
# 那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：
print(callable(my))
print(callable(max))
print(callable('ABC'))
print(callable(None))