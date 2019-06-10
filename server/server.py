import time
from socket import *
import threading

from other_functions.common_functions import msg_convert, find_sock

s = socket(AF_INET, SOCK_STREAM)
# from other_functions.stop_thread import stop_thread


socket_set = set()  # 用来保存每个socket对象
s.bind(('127.0.0.1', 9000))  # 绑定地址和端口
s.listen(5)
print('等待连接......')


def tcplink(sock, addr):
    host1, port1 = addr
    print('[%s:%s] 已上线' % addr)
    while True:
        try:
            data = sock.recv(1024).decode('utf-8')
            if not data:
                pass
            else:
                print('[%s:%s]:' % addr, data)
                senddata = data  # 收到的信息进行处理
                main_s = find_sock('9001', socket_set)
                # print(type(main_s), main_s)
                # print(socket_set)
                print(senddata)
                if main_s == None:
                    pass
                else:
                    main_s.send(senddata.encode('utf-8'))
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
            # for i in list1:
            #     i.send(data.encode())


def start_server(s):
    while True:
        # 接受一个客户端连接
        sock, addr = s.accept()  # addr是个元组('127.0.0.1',端口)
        socket_set.add(sock)  # 把socket对象添加到集合中
        # 创建新线程来处理TCP连接
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()

start_server(s)


