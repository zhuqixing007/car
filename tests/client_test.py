from socket import *
from threading import Thread

HOST = '127.0.0.1'
PORT = 9000
BUFFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.bind(('', 9002))
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

t1 = Thread(target=send)
t2 = Thread(target=recv)
t1.start()
t2.start()