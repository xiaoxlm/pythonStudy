# -*- coding: utf-8 -*-
#讲解判断和循环

a = '123'
a = int(a) #类型转换
print(a)

if isinstance(a, (int)):
	print('int')
else:
	print('not')

if a < 100 :
	print(a)
elif a > 110:
	print('elif')
else:
	print(-a)

list1 = ['jason', 'jack', 'daicy']

for name in list1:
	print(name)

#Python提供一个range()函数，可以生成一个整数序列, range(5)生成的序列是从0开始小于5的整数,再通过list()函数可以转换为list
print(list(range(5)))

n = 6

while n > 0:
	if n == 4:
		break  
	print(n)
	n = n - 2

while n > 0:
	n = n - 2
	if n == 4:
		continue
	print(n)
	