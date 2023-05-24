import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='test')
sql = "select * from test"
try:
    with conn.cursor() as cursor:
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)
    conn.commit()
except Exception as e:
    conn.rollback()

conn.close()