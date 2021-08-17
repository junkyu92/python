import pymysql

class DAO:

    # def __init__(self):
    #     con = pymysql.connect(host='localhost', port='3306', db='shop', user='root', password='1234')
    #     cur = con.cursor(pymysql.cursors.DictCursor)


    def create(vo):
        con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')

        cur = con.cursor(pymysql.cursors.DictCursor)

        sql = 'insert into member values (%s,%s,%s,%s)'
        result = cur.execute(sql, vo)

        con.commit()
        con.close()

        print(result)

    # def create(vo):
    #     con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    #     cur = con.cursor(pymysql.cursors.DictCursor)
    #
    #     sql = 'insert into member values(%s,%s,%s,%s)'
    #     result = cur.executemany(sql, vo)
    #
    #     con.commit()
    #     con.close()
    #
    #     print(result)

    def read(vo):
        con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
        cur = con.cursor(pymysql.cursors.DictCursor)

        sql = 'select * from member where id=%s'
        cur.execute(sql, vo)

        row = cur.fetchone()

        print(row)

        con.close()

    def update(vo):
        con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
        cur = con.cursor(pymysql.cursors.DictCursor)

        sql = 'update member set pw=%s where id=%s'
        cur.execute(sql, vo)

        con.commit()
        con.close()

    def delete(vo):
        con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
        cur = con.cursor(pymysql.cursors.DictCursor)

        sql = 'delete from member where id=%s'
        cur.execute(sql, vo)

        con.commit()
        con.close()

