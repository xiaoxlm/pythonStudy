# -*- coding: utf-8 -*-
# 主要讲解一些输出和字符串

print(r'\\') # 允许用r''表示''内部的字符串默认不转义

print('''1
2
3
	''') # 用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容

n = None # 空值是Python里一个特殊的值，用None表示。
print(n)

PI = 3.14156926 # 在Python中，通常用全部大写的变量名表示常量

chufa = 10//3 # 还有一种除法是//，称为地板除，两个整数的除法仍然是整数,整数的地板除//永远是整数，即使除不尽。要做精确的除法，使用/就可以
print(chufa)

print(ord('A')) # 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示
print(chr(65)) # chr()函数把编码转换为对应的字符

print('\u4e2d\u6587') # 知道字符的整数编码，还可以用十六进制这么写str

x = b'ABC' # Python对bytes类型的数据用带b前缀的单引号或双引号表示 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节
print(x)

print('中午'.encode('utf-8')) # 以Unicode表示的str通过encode()方法可以编码为指定的bytes

print(b'\xe4\xb8\xad\xe5\x8d\x88'.decode('utf-8'))#反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法

print(len('中文')) # 要计算str包含多少个字符，可以用len()函数

print('hello %s your have %d yuan' % ('jack', 10))

str = 'abc'

str2 = str.replace('ab', 'AB')  # 字符串的替换
print(str2)