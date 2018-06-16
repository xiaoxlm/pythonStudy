# -*- coding: utf-8 -*-
#使用dict和set

#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
d = {'lm':180, 'lz':175, 'yxc':160}
d['yoyo'] = 177
print(d['yoyo'])

print('lm' in d)  #通过in判断key是否存在
#dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
print(d.get('cv', 999))

#要删除一个key，用pop(key)方法，对应的value也会从dict中删除
d.pop('yoyo')
print(d)

#和list比较，dict有以下几个特点：
#查找和插入的速度极快，不会随着key的增加而变慢；
#需要占用大量的内存，内存浪费多。




#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。set是无序的,set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s = set([1,2,333,1,23,11])
s.add(333) #添加元素
s.add(76)  
s.remove(333) #删除元素
print(s) #重复元素在set中自动被过滤

s1 = set([1, 3, 555, 87])
s2 = set([2, 3, 555, 77])

print(s1 & s2) #交集
print(s1 | s2) #并集

