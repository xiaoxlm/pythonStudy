#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

# StringIO

# 很多时候，数据读写不一定是文件，也可以在内存中读写。

# StringIO顾名思义就是在内存中读写str。

# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：

from io import StringIO, BytesIO

str_io = StringIO()
str_io.write('hello')

print(str_io.getvalue()) # getvalue()方法用于获得写入后的str。

f = StringIO('Hello!\nHi!\nGoodbye!') # # 初始化在再写入的话会会覆盖初始化的内容
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())


print('\n')
# BytesIO

# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
b = BytesIO()
b.write('中文'.encode('utf-8')) # 请注意，写入的不是str，而是经过UTF-8编码的bytes。
print(b.getvalue())
print(b.getvalue().decode('utf-8'))


# 和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())

# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。