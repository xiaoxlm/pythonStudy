# -*- coding: utf-8 -*-
# 匿名函数

print(list( map( lambda x: x*x, [1,2,3] ) )) # 关键字lambda表示匿名函数，冒号前面的x表示函数参数

# lambda x: x*x 相当于
def f(x):
    return x * x

# 上面的代码相当于
print(list( map( f, [1,2,3] ) ))

# Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。
