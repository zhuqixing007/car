# 实时：视频图像采集(opencv)
import cv2
# 从视频流循环帧
def send_video():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.imshow("Frame", frame)
        # print(ret, frame)
        yield ret, frame
    #     # 退出：Q
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
    # # 清理窗口
    # cv2.destroyAllWindows()

video = send_video()
# print(video)
# for cap in video:
#     ret, frame = cap
#     cv2.imshow('frame', frame)

from socket import *
from threading import Thread

HOST = '127.0.0.1'
PORT = 9000
BUFFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
# tcpCliSock.bind(('', 9001))
tcpCliSock.connect(ADDR)
print(0)

def send():
    # print(1)
    for cap in video:
        # print(cap)
        ret, frame = cap
        tcpCliSock.sendall(cv2.imencode('.jpg', frame))
        # print(3)
    tcpCliSock.close()
    # print(4)

send()