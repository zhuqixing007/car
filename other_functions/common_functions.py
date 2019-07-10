import re

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

def msg_split(msg_sequent):
    pattern = re.compile('(\*.*?#)')
    msg_list = re.findall(pattern, msg_sequent)
    return msg_list

def find_sock(port, socket_set):
    for sock in socket_set:
        if port in str(sock):
            return sock
        else:
            return None



# str = """*D"device=smp1"#"""
# pattern1 = re.compile('\*([A-Z])"(.*)?"#')
# pattern2 = re.compile('\*.*?#')
# str2 = """*D"device=smp1"#*D"device=smp1"#*D"device=smp1"#"""
# m = re.match(pattern1,str)
# print(m.groups())
#
# m = re.findall(pattern2, str2)
# print(m)

# str = """*S"{'tem': 28, 'fire': 'ok', 'hum': 43, 'wifi_name': 'IOV', 'smoke': 0, 'RSSI': -34}"#*S"{'tem': 28, 'fire': 'ok', 'hum': 43, 'wifi_name': 'IOV', 'smoke': 0, 'RSSI': -34}"#"""
# msg = msg_split(str)
# for m in msg:
#     print(m)
#     if m:
#         print(msg_convert(m))