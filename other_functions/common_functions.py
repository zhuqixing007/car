

def msg_convert(msg):
    dic = eval(msg)
    return dic


def find_sock(port, socket_set):
    for sock in socket_set:
        if port in str(sock):
            return sock
        else:
            return None


