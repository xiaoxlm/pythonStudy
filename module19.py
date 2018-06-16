#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用模块
# 两种引入方式
# 第一种:
import module.hello
module.hello.test()

print(module.hello.__doc__) # hello模块定义的文档注释也可以用特殊变量__doc__访问

# 第二种
from module import hello

hello.test()

print(hello.__doc__)

# 在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。

# 正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等

# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；

# 之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。