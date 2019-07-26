from socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 9000))
sock.listen(5)

while True:
    s, addr = sock.accept()
    host, port = addr
    print('{}:{}已上线'.format(host, port))