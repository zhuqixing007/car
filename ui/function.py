# coding=utf-8
from other_functions.stop_thread import stop_thread
from server.server import start_server
from ui.desktop_ui import MyFrame1
from socket import *
import threading
import time


s = socket(AF_INET, SOCK_STREAM)
# socket_set = set()  # 用来保存每个socket对象
s.bind(('', 9000))  # 绑定地址和端口
s.listen(5)
server_thread = threading.Thread(target=start_server, args=(s,))
#


class ui_functions(MyFrame1):
    def __init__(self, parent):
        MyFrame1.__init__(self, parent)

    def MyFrame1OnClose(self, event):
        event.Skip()
        try:
            s.close()
            stop_thread(server_thread)
            HOST = '127.0.0.1'
            PORT = 9000
            ADDR = (HOST, PORT)
            tcpCliSock = socket(AF_INET, SOCK_STREAM)
            tcpCliSock.connect(ADDR)
        except:
            pass
        print('已退出')

    def openOnButtonClick(self, event):
        event.Skip()
        server_thread.start()
        self.m_textCtrl1.AppendText('服务器已开启\n')


    def closeOnButtonClick(self, event):
        event.Skip()
        try:
            s.close()
            stop_thread(server_thread)
            HOST = '127.0.0.1'
            PORT = 9000
            ADDR = (HOST, PORT)
            tcpCliSock = socket(AF_INET, SOCK_STREAM)
            tcpCliSock.connect(ADDR)
            self.m_textCtrl1.AppendText('服务器已关闭\n')
        except:
            self.m_textCtrl1.AppendText('关闭失败\n')

    def send_btnOnButtonClick(self, event):
        event.Skip()

    def refresh_btn2OnButtonClick(self, event):
        event.Skip()

