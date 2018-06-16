# 正则表达式

# re模块
import re
# Python提供re模块，包含所有正则表达式的功能。由于Python的字符串本身也用\转义，所以要特别注意。因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了
print(r'ss\ss', '\n')

res = re.match(r'^\d{3}-\d{3,8}$', '010-43244')
print(res)

# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。常见的判断方法就是:
test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')


res = 'a bc    c'.split(' ')  # 无法识别连续的空格
print(res)

print(re.split(r'\s+', 'a b    c  d'))


print(re.split(r'[\s,;]+', 'a,b  d;c e')) # 条件切割


# 分组
# 如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来。
m = re.match(r'(\d+)-(\d+)', '010-43243333')
print(m.groups())
print(m.group(0))
print(m.group(1))
print(m.group(2))
