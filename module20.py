#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 现在，让我们来安装一个第三方库——Python Imaging Library，这是Python下非常强大的处理图像的工具库。不过，PIL目前只支持到Python 2.7，并且有年头没有更新了，因此，基于PIL的Pillow项目开发非常活跃，并且支持最新的Python 3。
# 一般来说，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索，比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是

# pip install Pillow

# from PIL import Image
#
# im = Image.open('5005.jpg')
#
# print(im.format, im.size, im.mode)
#
# im.thumbnail((200, 100))
# im.save('thumb.jpg', 'JPEG')

import sys
print(sys.path) # Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量

# 如果我们要添加自己的搜索目录
# import sys
# sys.path.append('/Users/michael/my_py_scripts')
# 这种方法是在运行时修改，运行结束后失效。

# 第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。

# import MySQLdb
# conn = MySQLdb.connect(host = "172.16.60.12", user = "root", password = "rt@%12W*xy", database = "56CityExpress", charset = "utf8")
#
# cursor = conn.cursor()
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print(data);
# conn.close();
# import pymysql.cursors
# connection = pymysql.connect(host='172.16.60.12',
#                              user='root',
#                              password='rt@%12W*xy',
#                              db='56CityExpress',
#                              charset='utf8',
#                              cursorclass=pymysql.cursors.DictCursor)
#
# cursor = connection.cursor()
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print(data);
