# client

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for x in ['aaa', 'bbb', 'ccc']:
    s.sendto(x.encode('utf-8'), ('127.0.0.1', 8888))

    print(s.recv(1024).decode('utf-8'))

s.close()

# 客户端使用UDP时，首先仍然创建基于UDP的Socket，然后，不需要调用connect()，直接通过sendto()给服务器发数据：
# 从服务器接收数据仍然调用recv()方法。