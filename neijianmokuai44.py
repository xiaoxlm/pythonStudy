# collections

# collections是Python内建的一个集合模块，提供了许多有用的集合类。

# namedtuple
# 我们知道tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成：
#
# p = (1, 2)
# 但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。
#
# 定义一个class又小题大做了，这时，namedtuple就派上了用场：

from collections import namedtuple, deque, defaultdict, OrderedDict, Counter
# namedtuple('名称', [属性list]):
Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)
print(p.x)




# deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
print('\n')
q = deque(['a', 'b', 'c', 'd'])
q.append('x')
q.appendleft('y')
print(q)
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。




# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'

print(dd['key1'])
print(dd['key2']) # # key2不存在，返回默认值
# 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。




# OrderedDict

# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
#
# 如果要保持Key的顺序，可以用OrderedDict：

od = OrderedDict([('a', 1), ('b', 2), ('e', 6)]) # 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
od['z'] = 1

print(od)
print(list(od.keys())) # 按照插入的Key的顺序返回


print('\n')
# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        contains_key = 1 if key in self else 0
        if len(self) >= self._capacity:
            last = self.popitem(last = False)
            print('remove', last)

        if contains_key:
            del self[key]
            print('set', key, value)

        else:
            print('add', key, value)

        super(LastUpdatedOrderedDict, self).__setitem__(key, value)
        # 上面的语句等效于OrderedDict.__setitem__(self, key, value)

fifo = LastUpdatedOrderedDict(3)

fifo['yoyo'] = 3
fifo['yes'] = 4
fifo['yes'] = 10
fifo['xxx'] = 'rr'
fifo['s'] = 'aa'

print(fifo)



# Counter是一个简单的计数器，例如，统计字符出现的个数：
c = Counter()
for ch in "programmer":
    c[ch] += 1

print(c)

# Counter实际上也是dict的一个子类，上面的结果可以看出，字符'g'、'm'、'r'各出现了两次，其他字符各出现了一次







