"""
   ui_2的功能模块代码
"""
from other_functions.common_functions import msg_convert
from other_functions.stop_thread import stop_thread
from ui.ui_2 import MyFrame1
from socket import *
import threading



class ui_2_functions(MyFrame1):
    def __init__(self, parent):
        MyFrame1.__init__(self, parent)

    def MyFrame1OnClose(self, event):
        event.Skip()
        try:
            stop_thread(t)
            HOST = '127.0.0.1'
            PORT = 9000
            ADDR = (HOST, PORT)
            tcpCliSock = socket(AF_INET, SOCK_STREAM)
            tcpCliSock.connect(ADDR)
        except:
            pass

    def start_serverOnButtonClick(self, event):
        event.Skip()
        socket_set = set()
        def tcplink(sock, addr):
            host1, port1 = addr
            print('[%s:%s] 已上线' % addr)
            if port1 == 9001:
                print(port1)
                self.car1_state.SetLabelText('在线')
                self.m_textCtrl1.AppendText('1号车已上线\n')
            if port1 == 9002:
                print(port1)
                self.car2_state.SetLabelText('在线')
                self.m_textCtrl1.AppendText('2号车已上线\n')
            if port1 == 9003:
                print(port1)
                self.car3_state.SetLabelText('在线')
                self.m_textCtrl1.AppendText('3号车已上线\n')
            while True:
                try:
                    data = sock.recv(1024).decode('utf-8')
                    info = msg_convert(data)
                    if not data:
                        pass
                    else:
                        print('[%s:%s]: ' % addr, data)
                        self.m_textCtrl1.AppendText('[%s:%s]:' % addr)
                        self.m_textCtrl1.AppendText(data+'\n')
                        if port1 == 9001:
                            self.car1_tem.SetLabelText(str(info['tem']))
                            self.car1_hum.SetLabelText(str(info['hum']))
                        if port1 == 9002:
                            self.car2_tem.SetLabelText(str(info['tem']))
                            self.car2_hum.SetLabelText(str(info['hum']))
                        if port1 == 9003:
                            self.car3_tem.SetLabelText(str(info['tem']))
                            self.car3_hum.SetLabelText(str(info['hum']))
                        senddata = "received"  # 收到的信息进行处理
                        sock.send(senddata.encode())  # 将收到的信息返回给客户端
                except:
                    socket_set.remove(sock)
                    print('[%s:%s] 已下线!' % addr)
                    self.m_textCtrl1.AppendText('[%s:%s] 已下线\n' % addr)
                    if port1 == 9001:
                        self.car1_state.SetLabelText("离线")
                    if port1 == 9002:
                        self.car2_state.SetLabelText("离线")
                    if port1 == 9003:
                        self.car3_state.SetLabelText("离线")
                    break
                if data == 'exit' or not data:
                    socket_set.remove(sock)
                    sock.close()
                    print('[%s:%s] 已下线!' % addr)
                    self.m_textCtrl1.AppendText('[%s:%s] 已下线\n' % addr)
                    if port1 == 9001:
                        self.car1_state.SetLabelText("离线")
                    if port1 == 9002:
                        self.car2_state.SetLabelText("离线")
                    if port1 == 9003:
                        self.car3_state.SetLabelText("离线")
                    break
                else:
                    list1 = []
                    for i in socket_set:
                        if i != sock:
                            list1.append(i)
                    for i in list1:
                        i.send(data.encode())

        def start_server():
            s = socket(AF_INET, SOCK_STREAM)
            s.bind(('127.0.0.1', 9000))  # 绑定地址和端口
            s.listen(5)
            print('等待连接......')
            self.m_textCtrl1.AppendText('服务器已开启，等待连接中......\n')
            while True:
                # 接受一个客户端连接
                sock, addr = s.accept()  # addr是个元组('127.0.0.1',端口)
                socket_set.add(sock)  # 把socket对象添加到集合中
                # 创建新线程来处理TCP连接
                t = threading.Thread(target=tcplink, args=(sock, addr))
                t.start()
        global t
        t = threading.Thread(target=start_server)
        t.start()

    def start_all_carOnButtonClick(self, event):
        event.Skip()

    def shutdown_all_carOnButtonClick(self, event):
        event.Skip()

    def car1_sendOnButtonClick(self, event):
        event.Skip()

    def car1_startOnButtonClick(self, event):
        event.Skip()

    def car1_stopOnButtonClick(self, event):
        event.Skip()

    def car2_sendOnButtonClick(self, event):
        event.Skip()

    def car2_startOnButtonClick(self, event):
        event.Skip()

    def car2_stopOnButtonClick(self, event):
        event.Skip()

    def car3_sendOnButtonClick(self, event):
        event.Skip()

    def car3_startOnButtonClick(self, event):
        event.Skip()

    def car3_stopOnButtonClick(self, event):
        event.Skip()