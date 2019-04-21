from socket import *
import time
HOST = '127.0.0.1'
PORT = 9000
BUFFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.bind(('', 9002))
tcpCliSock.connect(ADDR)
while True:
    s = input('>')
    if s == 'quit':
        break
    else:
        tcpCliSock.sendall(bytes(s, encoding="utf-8"))
        accept_data = tcpCliSock.recv(1024)
        msg = str(accept_data, encoding="utf-8")
        print('from server：' + msg)
tcpCliSock.close()


