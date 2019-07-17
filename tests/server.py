from socket import *
from other_functions.common_functions import base64_to_img

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
    im = base64_to_img(data)
    with open("1111.jpg", "wb") as f:
        f.write(im)

