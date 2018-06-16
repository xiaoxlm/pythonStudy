# -*- coding:utf-8 -*-
# 返回函数

# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力
def lazy_sum(*argv):
    def sum():
        all = 0
        for n in argv:
            all += n
        return all
    return sum

f = lazy_sum(1, 3, 5, 6, 21)
print(f())

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
#你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是
print(f1()) # 9
print(f2()) # 9
print(f3()) # 9

# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。

# 这样改动就会达到想要的效果
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f())
    return fs

f1, f2, f3 = count()
print(f1) # 9
print(f2) # 9
print(f3) # 9