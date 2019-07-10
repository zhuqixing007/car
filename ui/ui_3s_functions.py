from ui.ui_3s import MyFrame1
from socket import *
import time
import threading



class ui_3s_functions(MyFrame1):
    def __init__(self, parent):
        MyFrame1.__init__(self, parent)

    def speed_sendOnButtonClick(self, event):
        event.Skip()

    def sample_sendOnButtonClick(self, event):
        event.Skip()

    def mapOnButtonClick(self, event):
        event.Skip()

    def visionOnButtonClick(self, event):
        event.Skip()

    def out_logOnButtonClick(self, event):
        event.Skip()

    def startOnButtonClick(self, event):
        HOST = '127.0.0.1'
        PORT = 9000
        BUFFSIZE = 1024
        ADDR = (HOST, PORT)

        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        tcpCliSock.bind(('', 9001))
        tcpCliSock.connect(ADDR)

        def send():
            s = input('>')
            while True:
                if s == 'quit':
                    break
                else:
                    tcpCliSock.sendall(bytes(s, encoding="utf-8"))
                s = input('>')
            tcpCliSock.close()

        def recv():
            while True:
                accept_data = tcpCliSock.recv(1024)
                msg = str(accept_data, encoding="utf-8")
                print("from server:" + msg)

        global t1, t2
        t1 = threading.Thread(target=send)
        t2 = threading.Thread(target=recv)
        t1.start()
        t2.start()

        event.Skip()

    def stopOnButtonClick(self, event):
        event.Skip()