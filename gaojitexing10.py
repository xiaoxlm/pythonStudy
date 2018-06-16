#-*- coding:utf-8 -*-
#迭代 可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）

L = [1, 2, 3, 55, 221, 566]
for v in L:
	print(v)
print("\t")

dic = {"a":12, "c":55, "ed":77}
for key in dic:
	print(key)  #只输出dict里面的key，同时key是无序输出

for value in dic.values(): 
	print(value) #输出dict里面的值，也是无序输出

from collections import Iterable  #引入collections模块的Iterable类型
res = isinstance('abc', Iterable) #判断是否可以迭代
print(res)

for index, value in enumerate({"a":12, "c":55, "ed":77}): #Python内置的enumerate函数可以把一个list变成索引-元素对
	print(index, '=', value)