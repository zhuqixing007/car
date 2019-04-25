
s = '''{'hum':56,'tem':12}'''


def msg_convert(msg):
    dic = eval(msg)
    return dic['hum'], dic['tem']



# print(msg_convert(s))