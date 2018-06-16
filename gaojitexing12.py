# -*- coding:utf-8 -*-
# 生成器
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了
# 那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
g = (x*x for x in range(10))
print(next(g)) # next()函数获得generator的下一个返回值
print(next(g))
print('\n')

# 斐波拉契数列
def fib(n):
    counter, a, b = 0, 0, 1
    while(counter < n):
        print(b)
        a, b = b, a+b
        counter += 1
    return 'done'

fib(6)

# odd函数变成一个generator对象
def odd():
    print('step 1')
    yield
    print('step 2')
    yield
    print('step 3')
    yield
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
# odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错。

o = odd()

next(o)
next(o)
next(o)

# 把fib变成生成器 要把fib函数变成generator，只需要加一个yield关键字就行
def fib_ger(n):
    counter, a, b = 0, 0, 1
    while(counter < n):
        yield b
        a, b = b, a+b
        counter += 1
    return 'done'

f = fib_ger(3)
next(f) # next不会输出yield后面的值

try:
    next(f)
    next(f)
    next(f)
except StopIteration as e:
    print('Generator return value:', e.value)

# 。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中

# 把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代
for n in fib_ger(6): # 迭代的就是yield后面的值 b
    print(n)

