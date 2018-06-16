# -*- coding:utf-8 -*-
# 列表生成式 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式
# 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))
print(list(range(1, 11)))

print([x*x for x in range(1, 11)])  # 生成[1x1, 2x2, 3x3, ..., 10x10]

print([x*x for x in range(1, 11) if x % 2 == 0])    # for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方

print([m+n for m in 'ABC' for n in 'abc'])  # 还可以使用两层循环

# 列出当前目录下的所有文件和目录名
import os   # 导入os模块

print([d for d in os.listdir('.')])

dic = {"x": "A", "cx": "qq", "ded": "dwq"}
for k, v in dic.items():
    print(k, '=', v)    # dict的items()可以同时迭代key和value。无序输出

print([k + '=' + v for k, v in {"x": "A", "cx": "qq", "ded": "dwq"}.items()])   # 这里+相当于字符串连接符

L = ['HDSA', 'DSCC', 'dFsxdF']

print([v.lower() for v in L])  # v.lower() for v in L  这段代码会返回一个generator对象，而[]将这个对象转换成集合