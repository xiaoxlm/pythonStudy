# -*- coding: utf-8 -*-
#讲解集合和元祖

#list 集合 list是可以变对象, 从排序中就可以看出来
list = ['sa', 1, 'dd', 'dd']#list是一种有序的集合，可以随时添加和删除其中的元素
print(list)

print(len(list))#用len()函数可以获得list元素的个数

print(list[0]) #用索引来访问list中每一个位置的元素，记得索引是从0开始
print(list[-1]) #如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引

list.append('Adam')#可以往list中追加元素到末尾
list.insert(1, '代替')#也可以把元素插入到指定的位置，比如索引号为1的位置
print(list)

list.pop()#删除list末尾的元素，用pop()方法
list.pop(0)#删除指定位置的元素，用pop(i)方法，其中i是索引位置

list[0] = 'keyi'#把某个元素替换成别的元素，可以直接赋值给对应的索引位置

s = ['ww', 'aa', [12, 555,113]]#list元素也可以是另一个list
print(s[2][1])

list = [2, 4, 1, 9]
list.sort()  #集合排序
print(list)


#tuple 有序列表元组, tuple和list非常类似，但是tuple一旦初始化就不能修改
tuple = ('lm', 'lxq', 'hehe') #它没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用tuple[0]，tuple[-1]，但不能赋值成另外的元素。因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
print(tuple[-1])

#因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。所以，只有1个元素的tuple定义时必须加一个逗号,来消除歧义
tuple1 = (1,)
print(tuple1) 

#tuple里面的list元素可以变 例:
tuple3 = (1, 2, ['x', 'y'])
#tuple3[0] = 's';  这会报错
tuple3[2][1] = 'a' #这样就不会报错， 因为你改变的其实是list数据类型
print(tuple3)  

#可以这样用tuple和list赋值
x, y = (666, 2) 
x, y = [666, 2]  
print(x)