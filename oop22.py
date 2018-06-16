#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 获取对象信息

# 我们来判断对象类型，使用type()函数

print(type(123))

# 但是type()函数返回的是什么类型呢？它返回对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同

if(type(123) == type(666)):
    print('class is same')


# 但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
import types

def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)
print('\n')

class Animal:
    pass

animal = Animal()
print(type(animal))



# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数
class Dog(Animal):
    pass

d = Dog()
print( isinstance(d, Dog) and isinstance(d, Animal) )

# 能用type()判断的基本类型也可以用isinstance()判断
print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))
print('\n')
# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
print(isinstance([1, 2, 3], (list, tuple, dict)))
print(isinstance((1, 2, 3), (list, tuple)))



# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
print(dir('ADC'))
print('ADC'.__len__())


# 在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
len('ABC')
'ABC'.__len__()


# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法:
class MyObj(object):
    def __len__(self):
        return 100

my_obj = MyObj()
print(len(my_obj))
print('\n')


# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()
print(hasattr(obj, 'x')) # 有属性'x'吗？

setattr(obj, 'y', 19) # 设置一个属性'y'
getattr(obj, 'y') # 获取属性'y'
print(getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404

hasattr(obj, 'power') # 有属性'power'吗？

fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn。 fn指向obj.power
print(fn)
print(fn())

# # 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：
#
# sum = obj.x + obj.y
# # 就不要写：
#
# sum = getattr(obj, 'x') + getattr(obj, 'y')
# # 一个正确的用法的例子如下：
#
# def readImage(fp):
#     if hasattr(fp, 'read'): # 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。
#         return readData(fp)
#     return None

class Test(object):
    ok = 'yoyo'
    def wo(self):
        print(self.ok)

t = Test()
t.wo();