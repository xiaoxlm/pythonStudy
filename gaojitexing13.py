# -*- coding: utf-8 -*-
# 我们已经知道，可以直接作用于for循环的数据类型有以下几种：
#
# 一类是集合数据类型，如list、tuple、dict、set、str等；
#
# 一类是generator，包括生成器和带yield的generator function。
#
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
#
# 可以使用isinstance()判断一个对象是否是Iterable对象：

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
#
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：

string = 'ABC'
string = iter(string)
print(next(string))

# 凡是可作用于for循环的对象都是Iterable类型；
#
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。