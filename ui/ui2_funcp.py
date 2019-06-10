"""
   ui_2的功能模块代码
"""
from other_functions.common_functions import msg_convert
from other_functions.stop_thread import stop_thread
from ui.ui_2 import MyFrame1
from socket import *
import threading



class ui2_cp(MyFrame1):
    def __init__(self, parent):
        MyFrame1.__init__(self, parent)

    def MyFrame1OnClose(self, event):
        event.Skip()
        try:
            stop_thread(t2)
            tcpCliSock.close()
        except:
            pass


    def start_serverOnButtonClick(self, event):
        event.Skip()

    def start_all_carOnButtonClick(self, event):
        event.Skip()

    def shutdown_all_carOnButtonClick(self, event):
        event.Skip()

    def car1_sendOnButtonClick(self, event):
        event.Skip()

    def car1_startOnButtonClick(self, event):
        self.car1_state.SetLabelText('已连接')
        HOST = '127.0.0.1'
        PORT = 9000
        BUFFSIZE = 1024
        ADDR = (HOST, PORT)

        global tcpCliSock
        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        tcpCliSock.bind(('', 9001))
        tcpCliSock.connect(ADDR)

        # def send():
        #     s = input('>')
        #     while True:
        #         if s == 'quit':
        #             break
        #         else:
        #             tcpCliSock.sendall(bytes(s, encoding="utf-8"))
        #         s = input('>')
        #     tcpCliSock.close()


        def recv():
            while True:
                accept_data = tcpCliSock.recv(BUFFSIZE)
                msg = str(accept_data, encoding="utf-8")
                print(msg)
                self.m_textCtrl2.AppendText(msg+'\n')
                # msg = msg.split(":")
                # info = msg_convert(msg)
                # print(info['tem'])

        global t2
        # t1 = threading.Thread(target=send)
        # t1.start()
        t2 = threading.Thread(target=recv)
        t2.start()

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