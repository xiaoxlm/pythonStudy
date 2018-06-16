# hashlib

import hashlib

md5 = hashlib.md5()
md5.update('ddd'.encode('utf-8'))
print(md5.hexdigest())

# 6, 7 行的代码 相当于php  print_r(md5('ddd'))