from socket import *
import threading
from other_functions.common_functions import *



s = socket(AF_INET, SOCK_STREAM)
socket_set = set()  # 用来保存每个socket对象
supervise_set = set()  # 保存客户端socket对象
smp_set = set()  # 保存小车上连接服务器的设备socket对象

s.bind(('', 9000))  # 绑定地址和端口
s.listen(20)  # 设置服务器监听数量
print('等待连接......')


def tcplink(sock, addr):
    """服务器tcp连接监听建立函数"""
    host1, port1 = addr  # 获取IP地址和端口号
    data = sock.recv(1024).decode('utf-8')  # 连接之后第一条消息为设备名验证消息
    # print(data)
    if msg_convert(data)[0] == "D":
        pattern1 = re.compile('device=(.*)')
        device = re.findall(pattern1, msg_convert(data)[1])[0]  # 获取设备名
        print('%s 已上线' % device)

        """PC客户端socket对象"""
        if device == 'daddy':
            supervise_set.add(sock)
            # print(daddy)

        """手机客户端socket对象"""
        if device == "phone":
            supervise_set.add(sock)

        """小车上树莓派socket对象"""
        if device == "smp":
            smp_set.add(sock)

        while True:
            """开始循环监听"""
            try:
                data = sock.recv(10240000).decode('utf-8')  # 为了能够传输图片，recv()中的参数尽量设置大一点
                if not data:
                    pass  # 消息内容为空，不做处理
                else:
                    # print('[%s:%s]:' % addr, data)
                    for sk in supervise_set:
                        """将小车树莓派发送消息转发到客户端平台"""
                        if sk != sock:  # 避免自生发送造成网络堵塞
                            sk.send(data.encode("utf-8"))

                    for sk in smp_set:  # 避免自生发送造成网络堵塞
                        """将客户端发送消息转发到小车上相应的树莓派"""
                        if sk != sock:
                            sk.send(data.encode("utf-8"))

            except:
                """连接发生异常后从相应的socket对象集合中移除当前连接对象"""
                socket_set.remove(sock)
                if sock in supervise_set:
                    supervise_set.remove(sock)
                if sock in smp_set:
                    smp_set.remove(sock)
                print('%s 已下线' % device)
                break

            if data == 'exit' or not data:
                """设备下线后，从相应的socket集合中移除当前socket对象"""
                socket_set.remove(sock)
                if sock in supervise_set:
                    supervise_set.remove(sock)
                if sock in smp_set:
                    smp_set.remove(sock)
                sock.close()
                print('%s 已下线' % device)
                break
    else:
        socket_set.remove(sock)
        print("已拒绝向未授权地址 [%s:%s] 提供数据连接服务。" % addr)

def start_server(s):
    while True:
        # 接受一个客户端连接
        sock, addr = s.accept()  # addr是个元组('127.0.0.1',端口)
        socket_set.add(sock)  # 把socket对象添加到集合中
        # 创建新线程来处理TCP连接
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()

start_server(s)


