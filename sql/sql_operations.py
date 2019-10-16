import pymysql


def insert_into_sensor_data(values):
    """接受参数为一个元组，元组元素顺序为时间，车速，温度，明火，烟雾"""
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


def consult_seneor_data():
    db = pymysql.connect("localhost", "root", "root", "db_3s")
    cursor = db.cursor()
    sql = 'select * from sensor_data'
    cursor.execute(sql)
    results = cursor.fetchall()
    db.commit()
    db.close()
    return results

def query_last(time):
    db = pymysql.connect("localhost", "root", "root", "db_3s")
    cursor = db.cursor()
    sql = "select * from sensor_data where 时间='%s'"%time
    cursor.execute(sql)
    results = cursor.fetchall()
    db.commit()
    db.close()
    return results
