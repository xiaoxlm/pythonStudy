# TCP 编程
# server

# 和客户端编程相比，服务器编程就要复杂一些。

# 服务器进程首先要绑定一个端口并监听来自其他客户端的连接。如果某个客户端连接过来了，服务器就与该客户端建立Socket连接，随后的通信就靠这个Socket连接了。

# 所以，服务器会打开固定端口（比如80）监听，每来一个客户端连接，就创建该Socket连接。由于服务器会有大量来自客户端的连接，所以，服务器要能够区分一个Socket连接是和哪个客户端绑定的。一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket。

# 但是服务器还需要同时响应多个客户端的请求，所以，每个连接都需要一个新的进程或者新的线程来处理，否则，服务器一次就只能服务一个客户端了。



# 实现了 聊天功能！！！
import socket, threading, time

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    ss = str(addr).strip('()')  # s.strip().lstrip().rstrip(',') 去除特殊字符

    sock.send(('welcome! %s' % ss).encode('utf-8'))
    # sock.send(b'welcome! %s' % ss.encode('utf-8')) # encode将字符串转换成字节类型的。 以Unicode表示的str通过encode()方法可以编码为指定的bytes
    while True:
        data = sock.recv(1024)
        print(data.decode('utf-8'))
        time.sleep(1)

        if not data or data.decode('utf-8') == 'exit':
            break   # 如果客户端断开连接后，data会为空
        input_msg = input('enter message: ')
        sock.send(('server: ' + input_msg).encode('utf-8'))
    sock.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 创建socket

s.bind(('172.16.20.99', 7777))  # 绑定地址，端口

s.listen(5) # 指定等待连接的最大数量

print('waiting for connction...')


while True:
    sock, addr = s.accept() # 接受一个连接
    t = threading.Thread(target = tcplink, args=(sock, addr)) # 创建一个线程来处理TCP连接
    t.start()



# 用TCP协议进行Socket编程在Python中十分简单，对于客户端，要主动连接服务器的IP和指定端口，对于服务器，要首先监听指定端口，然后，对每一个新的连接，创建一个线程或进程来处理。通常，服务器程序会无限运行下去。
#
# 同一个端口，被一个Socket绑定了以后，就不能被别的Socket绑定了。




