# client

import socket, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('172.16.20.99', 7777))

# print(s.recv(1024).decode('utf-8'))

# 实现了聊天功能！！！

while True:
    print(s.recv(1024).decode('utf-8'))  # 如果没有接收到消息，recv()会一直阻塞等待, 直到有消息来
    input_msg = input('enter message: ')
    s.send(('client: ' + input_msg).encode('utf-8'))
    time.sleep(1)


# for data in [b'jack', b'rose', b'lee']:
#     s.send(data)
#     print(s.recv(1024).decode('utf-8'))
#
# s.send(b'exit')
s.close()