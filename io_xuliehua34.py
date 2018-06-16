#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

# 在程序运行的过程中，所有的变量都是在内存中，比如，定义一个dict：
d = dict(name = 'bob', age = 20, score = 88)
# 可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。如果没有把修改后的'Bill'存储到磁盘上，下次重新运行程序，变量又被初始化为'Bob'。

# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

# Python提供了pickle模块来实现序列化。Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。

import pickle, shutil
# print(pickle.dumps(d)) # ickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
# shutil.copyfile('mm.txt', 'bytes.txt')
# serilize_byte = pickle.dumps(d)
# f = open('mm.txt', 'ab') # 以字节形式写入读取
# f.write(serilize_byte)
# f.close()
# f = open('bytes.txt', 'a+b')
# pickle.dump(d, f) # 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
# f.close()
# 看看写入的bytes.txt文件，一堆乱七八糟的内容，这些都是Python保存的对象内部信息。

# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。我们打开另一个Python命令行来反序列化刚才保存的对象：

f = open('mm.txt', 'rb')
dic = pickle.load(f)
f.close()
print(type(dic))


# Json
import json

json_data = json.dumps(d) # 相当于php的json_encode
print(type(json_data))  # python内置的json模块提供了非常完善的Python对象到JSON格式的转换。dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。

# 由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换。
print(type(json.loads(json_data))) # 相当于php的json_decode



# 很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化
# 默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可, 不然会直接json.dumps(obj)会报错

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 18, 99)

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

obj_json = json.dumps(s, default=student2dict)
print(type(obj_json), 'yoyo')


# 不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
json_str = json.dumps(s, default=lambda obj: obj.__dict__)
print(type(json_str))
# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。


# 样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例。
json_str = '{"name": "sss", "age": 18, "score": 97}'
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

res = json.loads(s=json_str, object_hook=dict2student) # 打印出的是反序列化的Student实例对象。
print(res)


# python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。

# json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，既做到了接口简单易用，又做到了充分的扩展性和灵活性。