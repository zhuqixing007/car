from ui.map_pygame import car_map
from ui.ui_3s import MyFrame1
from socket import *
import threading
import re
import os


class ui_3s_functions(MyFrame1):
    def __init__(self, parent):
        MyFrame1.__init__(self, parent)
        self.connect_flag = 0
        self.HOST = ''
        self.PORT = 0

    def MyFrame1OnClose(self, event):
        os._exit(0)
        event.Skip()

    def speed_sendOnButtonClick(self, event):
        event.Skip()

    def sample_sendOnButtonClick(self, event):
        event.Skip()

    def mapOnButtonClick(self, event):
        t = threading.Thread(target=car_map)
        t.start()
        event.Skip()

    def visionOnButtonClick(self, event):
        event.Skip()

    def out_logOnButtonClick(self, event):
        event.Skip()

    def startOnButtonClick(self, event):
        HOST = self.ip.GetValue()
        PORT = self.port.GetValue()
        pattern1 = re.compile('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+')
        pattern2 = re.compile('[0-9]+')
        match1 = re.match(pattern1, HOST)
        match2 = re.match(pattern2, PORT)

        def send(tcpCliSock):
            s = input('>')
            while True:
                if s == 'quit':
                    break
                else:
                    tcpCliSock.sendall(bytes(s, encoding="utf-8"))
                s = input('>')
            tcpCliSock.close()

        def recv(tcpCliSock):
            while True:
                accept_data = tcpCliSock.recv(1024)
                msg = str(accept_data, encoding="utf-8")
                print("from server:" + msg)

        if match1:
            if match2:
                if int(PORT) < 65535 and int(PORT) > 0:
                    self.log.AppendText('尝试连接{}:{}。'.format(HOST, PORT)+'\n')
                    if self.connect_flag == 0:
                        self.PORT = int(PORT)
                        self.HOST = HOST
                        try:
                            ADDR = (self.HOST, self.PORT)
                            tcpCliSock = socket(AF_INET, SOCK_STREAM)
                            tcpCliSock.connect(ADDR)
                        except:
                            self.log.AppendText("连接失败，请检查地址和端口号是否正确或者服务器是否开启。\n")
                        else:
                            self.connect_flag = 1
                            global t1, t2
                            t1 = threading.Thread(target=send, args=(tcpCliSock,))
                            t2 = threading.Thread(target=recv, args=(tcpCliSock,))
                            t1.start()
                            t2.start()
                        try:
                            tcpCliSock.sendall(bytes("""*D"device=daddy"#""", encoding="utf-8"))
                        except:
                            pass
                        else:
                            self.log.AppendText("与服务器连接成功。\n")
                    elif self.connect_flag == 1:
                        self.log.AppendText("已与服务器建立连接，请不要重复连接。\n")
                    else:
                        pass
                else:
                    self.log.AppendText('请输入正确端口号。\n')
            else:
                self.log.AppendText('请输入正确端口号。\n')
        else:
            self.log.AppendText('请输入正确IP地址。\n')

        event.Skip()

    def stopOnButtonClick(self, event):
        event.Skip()