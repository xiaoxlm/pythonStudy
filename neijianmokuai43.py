# datetime

# datetime是Python处理日期和时间的标准库。

from datetime import datetime, timedelta
now = datetime.now() # 获取当前时间
print(now)
print(type(now))

# 注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。
#
# 如果仅导入import datetime，则必须引用全名datetime.datetime。
#
# datetime.now()返回当前日期和时间，其类型是datetime。


# 要指定某个日期和时间，我们直接用参数构造一个datetime
dt = datetime(2016, 10, 19, 14, 6, 55)
print(dt)



# timestamp
# timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的，这就是为什么计算机存储的当前时间是以timestamp表示的，因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）。

# 一个datetime类型转换为timestamp只需要简单调用timestamp()方法：
print(dt.timestamp())



# timestamp转换为datetime
#
# 要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法
timestamp = dt.timestamp()
print(datetime.fromtimestamp(timestamp))

# timestamp也可以直接被转换到UTC标准时区的时间：
print(datetime.utcfromtimestamp(timestamp))



# str转换为datetime

# 很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：
print('\n')
time = '2016-10-19 14:13:55'
cday = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
print(cday)



# datetime转换为str

# 如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串：
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))



# datetime加减

# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：
change_time1 = now + timedelta(hours=1)
print(change_time1)


change_time2 = now - timedelta(days=1, hours=3, minutes=2, seconds=10)
print(change_time2)