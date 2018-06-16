#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

# @property

# Python内置的@property装饰器就是负责把一个方法变成属性调用的， 其实就相当于方法重载但必须加上@

class Student(object):

    @property # 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
    def name(self):
        return self._name

    @property # 把一个方法变成getter属性，只需要加上@property就可以
    def score(self):
        return self._score   # 切记属性名不能跟方法名一样

    @score.setter # @score.setter，负责把一个setter方法变成属性赋值; 要用@方法.setter前，必须在该方法前 加上@property
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be integer!")

        if value < 0 or value > 100:
            raise ValueError("score must be between 0 and 100")

        self._score = value



stu = Student()
stu.score = 10
print(stu.score)

# stu.name = 'name'  # 会报错，name是只读属性，不能赋值




# 多继承(MixIn)
class Animal(object):
    pass

class Mammal(Animal):
    pass

class Flyable(object):
    def fly(self):
        print('flying...')

class Bat(Mammal, Flyable):
    pass

bat = Bat()
bat.fly()

# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。

# 由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
# 只允许单一继承的语言（如Java）不能使用MixIn的设计。
