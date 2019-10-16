from socket import *
from threading import Thread
import time

HOST = '129.204.16.212'
PORT = 9000
BUFFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)


def send():
    tcpCliSock.sendall(bytes("""*D"device=smp"#""", encoding="utf-8"))
    i = 1
    k = 2
    while True:
        if i < 90:
            s = """*S"{'tem': """ + str(i) + """, 'fire': 'ok', 'hum': """ + str(
                k) + """, 'wifi_name': 'IOV', 'smoke': 0, 'RSSI': -34}"#"""
            tcpCliSock.sendall(bytes(s, encoding="utf-8"))
            i += 1
            k += 3
            time.sleep(1)
        else:
            break

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
