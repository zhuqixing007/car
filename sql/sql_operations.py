import re

import pymysql
import datetime
import time

def insert(table, value):
    db = pymysql.connect("localhost", "root", "123", "car")
    cursor = db.cursor()
    time_value = str(datetime.datetime.now())
    # sql = 'INSERT INTO car_control_interface_data_receive(body,timestamp1)VALUES(' \
    #       + "'" + value + "'" + ',' + "'" + time_value + "'" + ')'
    # cursor.execute(sql)
    db.commit()
    db.close()

def check_update():
    file = open('/var/log/mysql/mysql.log')
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def get_changed_data():
    log = check_update()
    for line in log:
        str1 = line.strip('\n')
        if 'INSERT' in str1 and 'car_control_interface_data_send' in str1:
            str2 = str1.split('VALUES')
            pattern = re.compile(r'\'(.*?)\',', re.S)
            msg = re.findall(pattern, str2[1])
            print(msg[0])
            return '*' + msg[0].rstrip('/') + '#'
            #return '*' + str2[1] + '#'