from socket import *
import threading
from other_functions.common_functions import find_sock, msg_convert



s = socket(AF_INET, SOCK_STREAM)
socket_set = set()  # 用来保存每个socket对象
s.bind(('', 9000))  # 绑定地址和端口
s.listen(5)
print('等待连接......')


def tcplink(sock, addr):
    host1, port1 = addr
    data = sock.recv(1024).decode('utf-8')
    # print(data)
    device = msg_convert(data)
    print('%s 已上线' % device)
    if device == 'daddy':
        daddy = port1
        # print(daddy)
    daddy_sock = find_sock(daddy, socket_set)
    while True:
        try:
            data = sock.recv(10240000).decode('utf-8')
            if not data:
                pass
            else:
                print('[%s:%s]:' % addr, data)
                senddata = data  # 收到的信息进行处理
                # print(0)
                # print(1)
                if daddy_sock:
                    # print(2)
                    if daddy_sock != sock:
                        daddy_sock.send(senddata.encode('utf-8'))
                    else:
                        pass
                if daddy_sock == sock:
                    for s in socket_set:
                        if daddy_sock == s:
                            pass
                        else:
                            s.send(senddata.encode('utf-8'))
                else:
                     sock.send('收到'.encode('utf-8'))

        except:
            socket_set.remove(sock)
            print('[%s:%s] 已下线!' % addr)
            break
        if data == 'exit' or not data:
            socket_set.remove(sock)
            sock.close()
            print('[%s:%s] 已下线!' % addr)
            break
        else:
            list1 = []
            for i in socket_set:
                if i != sock:
                    list1.append(i)


def start_server(s):
    while True:
        # 接受一个客户端连接
        sock, addr = s.accept()  # addr是个元组('127.0.0.1',端口)
        socket_set.add(sock)  # 把socket对象添加到集合中
        # 创建新线程来处理TCP连接
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()

start_server(s)


