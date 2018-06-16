#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 偏函数
# int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换
print(int('12', base=16)) # 把16进制的数转换成10进制
print(int('0100', base=2))
print(int('0100', **{'base': 2})) # 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数


from functools import partial

# functools.partial就是帮助我们创建一个偏函数的，
int2 = partial(int, base=2)
print(int2('10010'))  # 所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

max2 = partial(max, 10)  # 实际上会把10作为*args的一部分自动加到左边
print(max2(1, 2, 8))
# 上面代码相当于
args = (10, 1, 2, 8)
max(*args)

# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。