# -*- coding: utf-8 -*-
# 高阶函数 编写高阶函数，就是让函数的参数能够接收别的函数。 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
# 函数名其实就是指向函数的变量！对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数
# list = 1
# list(range(10))
# 这样就会报错，因为你将list 不再是指向一个函数， 而指向了整数1

#传入函数
def add(x, y, f):
    return f(x) + f(y)

print(add(10, -6, abs))



# map/reduce

# map 作用单个元素
def f(x):
    return x * x

r = map(f, [1,2,3,4,5,6]) # 返回一个map object
print(list(r)) # 输出 [1, 4, 9, 16, 25, 36]

# reduce 把结果继续和序列的下一个元素做累积计算
from functools import reduce
def my_sum(x, y):
    return x + y

print(reduce(my_sum, [1, 2, 3, 4, 5])) # 输出15


# filter  filter()函数用于过滤序列
# filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素


# sorted 排序算法
# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
print(sorted([35, -98, 33, 23, -3], key = abs))
# 按字符串长度排序
print(sorted(['Bob', 'amazing', 'yes', 'Noah'], key = str.__len__))
# 排序忽略大小写
print(sorted(['Bob', 'amazing', 'yes', 'Noah'], key = str.lower))
# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(['Bob', 'amazing', 'yes', 'Noah'], key = str.lower, reverse = True))

from operator import itemgetter
#将学生安成绩排序
student = [('Jack', 89), ('Bob', 75), ('Tom', 66)]
print(sorted(student, key = itemgetter(1)))
print(sorted(student, key=lambda t: t[1]))

from collections import Iterable
student = {'Jack': 89, 'Bob': 75, 'Tom': 66}
print( isinstance(student, Iterable) )
print(sorted(student.items(), key = lambda dic: dic[1]))

print(student.values())




