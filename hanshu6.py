#-*- coding: utf-8 -*-
#调用函数
a = -100 
print(abs(a)) #绝对值

print(max([1, 2, 5, 10]))
print(max(1, 2, 5, 10))

#数据类型装换
str(1.23)
float('1.23')
int('22')
bool(1)	#True
bool('') #False

#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs
print(a(-1))

print(hex(123))



#定义函数
def my_abs(x):
	if not isinstance(x, (float, int)):	#数据类型检查可以用内置函数isinstance()实现, 这不能用！表示非，得用not
		raise TypeError('数据类型错误')  #抛出异常
	if x >= 0:
		return x
	else:
		return -x

print(my_abs(-111))

#如果想定义一个什么事也不做的空函数，可以用pass语句。实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来
def pop():
	pass

import math #引入math包

def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny   #函数返回多个值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便

x, y = move(100, 200, 60, math.pi/6)  #返回多个值得函数 赋值给多个变量
print(x, y)

n = move(100, 200, 60, math.pi/6) #n是一个tuple
print(n)


