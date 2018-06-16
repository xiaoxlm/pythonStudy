#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
class Student(object):
    pass

stu = Student()



# 给stu实例绑定一个方法
import types

def _set_age(self, age): # 定义一个函数作为实例方法
    self.age = age
    return self.age

stu.set_age = types.MethodType(_set_age, stu) # 给实例绑定一个方法
stu.set_age(44)

print(stu.age)




# 给一个实例对象绑定的方法，对另一个实例对象是不起作用的。为了给所有实例都绑定方法，可以给class绑定方法
stu3 = Student()
def _set_score(self, score):
    self.score = score

Student.set_score = _set_score # 给class绑定方法后，所有实例均可调用
# 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。

stu3.set_score(66)  # stu3这个对象时在添加set_score之前创建的对象， 但也能用上set_score
print(stu3.score)




# 使用__slots__
# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

class Person(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

p = Person()
p.name = 'aaa'
p.age = 18
# p.height = 180 # 报错， 因为__slots__里面只有name和age，所以实例只能给这两个属性赋值

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class Chinese(Person):
    pass

ch = Chinese()
ch.height = 180

# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
class American(Person):
    __slots__ = ('height', 'sex')

american = American()
american.height = 180
american.name = 'Jack'
