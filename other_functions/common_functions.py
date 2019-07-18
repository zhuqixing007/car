import re
import time
import base64

"""解析消息"""
def msg_convert(msg):
    pattern = re.compile('\*([A-Z])"(.*)?"#')
    m = re.match(pattern, msg)
    msg = m.groups()
    if msg[0] == 'D':
        pattern1 = re.compile('device=(.*)')
        device = re.findall(pattern1, msg[1])[0]
        return device
    else:
        dic = eval(msg[1])
        return dic


"""逐条分离消息队列中的消息"""
def msg_split(msg_sequent):
    pattern = re.compile('(\*.*?#)')
    msg_list = re.findall(pattern, msg_sequent)
    return msg_list


"""查找指定端口号"""
def find_sock(port, socket_set):
    for sock in socket_set:
        if str(port) in str(sock):
            return sock
        else:
            return None


"""检查文件更新内容"""
def check_update(filename):
    file = open(filename, 'r+')
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.001)
            continue
        yield line


def base64_to_img(base64_data):
    pattern = re.compile(r"""b'(.*?)'""")
    # print(base64_data)
    img_data = re.findall(pattern, base64_data)[0]
    # print(img_data)
    img = base64.b64decode(img_data)
    return img