from socket import *
from other_functions.common_functions import base64_to_img
import cv2
import time
import base64

s = socket(AF_INET, SOCK_STREAM)
s. bind(('', 8000))
s.listen(5)
print("等待连接...")


while True:
    sock, addr = s.accept()
    host, port = addr
    print('{0}:{1}已上线。'.format(host, port))
    data = sock.recv(1024000).decode("utf-8")
    print(data)
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        k = cv2.waitKey(1)
        if k == 27:
            break
        elif k == ord('s'):
            cv2.imwrite('1.jpg', frame)
            with open("1.jpg", "rb") as f:
                img = f.read()
                base64_data = base64.b64encode(img)
            sock.sendall(bytes(str(base64_data), encoding="utf-8"))
        cv2.imshow('cam', frame)

    cap.release()
    cv2.destroyAllWindows()

    # im = base64_to_img(data)
    # with open("1111.jpg", "wb") as f:
    #     f.write(im)


