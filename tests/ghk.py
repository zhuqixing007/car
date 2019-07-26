import base64
from socket import *
import re

s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 9000))

with open("123.jpg", "rb") as f:
    img = f.read()
    base64_data = base64.b64encode(img)
    print(base64_data)
    # print(type(base64_data))

s.sendall(bytes(str(base64_data), encoding="utf-8"))
s.close()
