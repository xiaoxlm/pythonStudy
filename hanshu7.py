#-*- coding: utf-8 -*-
#函数参数讲解
def power(x, n=2, desc = 'hehe'):  #参数设置默认值
	s = 1
	while n > 0 :
		n = n - 1
		s = s * x
	return s, desc

print(power(3, desc = '666'))  #指定函数参数赋值  #从哪一个实参指定了参数名，其后面的所有实参都必须指定参数名；


#一个坑
def add_end(L = []):
	L.append('end')
	return L

print(add_end())
print(add_end())
print(add_end())
#打印结果是:
#['end']
#['end', 'end']
#['end', 'end', 'end']
#因为:
#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
#修改上面函数
def add_end(L = None):
	if L is None: #判断变量是否为None
		L = []
		L.append('end')
	return L

print(add_end())
print(add_end())
print(add_end())


#可变参数 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum += n
	return sum
print(calc())
print(calc(1, 2, 3))
print(calc(*[1, 2, 3])) #Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
print(calc(*(1, 2, 3)))



#关键字参数  关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age=18, **argv):  
	print('name: %s, age: %d' % (name, age), 'other:', argv )
	return None

person('lm', 18, city='北京', ar=3) #关键字参数必须带关键字， 也就是以这种方式传递参数key=value

person('lm', 18, **{'city':'北京', 'school':'CD'}) #把该dict转换为关键字参数传进去



#命名关键字参数
#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下
def pp(name, age, *, city = 'CD', job):   # * 后面的参数 在传入时必须指定键值
	print(name, age, city, job)

pp('aa', 15, city='cd', job='php')  #如果不指定city， job键值就会报错
pp('aa', 15, job='php')


#组合参数
#Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。



def func(a, b, *argv, **dic):
	print('a:', a, 'b:', b, 'argv: ', argv, 'dic: ', dic)


tup = (1, 2, 4)
dic = {'xx':12, 'cc':'ccde'}

func(*tup, **dic)

func(3, 4, 5, 6, 8, 9)

#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的


