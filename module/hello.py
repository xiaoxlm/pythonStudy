#!/usr/bin/env python3     第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行
# -*- coding: utf-8 -*-    第2行注释表示.py文件本身使用标准UTF-8编码

' a test module '    # 表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'LM'  # 使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名

# 以上就是Python模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错。

import sys

def test():
    argv = sys.argv # sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称。例如：运行python3 hello.py获得的sys.argv就是['hello.py']；
    if len(argv) == 1:
        print('hello world')
    elif len(argv) == 2:
        print('hello', argv[1])
    else:
        print('too many arguments')

# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
if __name__ == '__main__':
    test()

