import re

import pymysql
import datetime
import time


def insert_into_sensor_data(values):
    """接受参数为一个元组，元组包含"""
    db = pymysql.connect("localhost", "root", "root", "db_3s")
    cursor = db.cursor()
    try:
        sql = "create table sensor_data(时间 varchar (20), 车速 VARCHAR (3), 温度 varchar (2), " \
              "湿度 varchar (2), 明火 varchar (3), 烟雾 VARCHAR (3))"
        cursor.execute(sql)
    except pymysql.err.InternalError:
        pass
    sql = 'INSERT INTO sensor_data(时间, 车速, 温度, 湿度, 明火, 烟雾) VALUES (%s,%s,%s,%s,%s,%s)'
    cursor.execute(sql, values)
    db.commit()
    db.close()


# insert_into_sensor_data(('2019-07-14 21:29', '0', '28', '32', '无', '无'))