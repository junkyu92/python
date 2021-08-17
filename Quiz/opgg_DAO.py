import pymysql

class Opgg:
    def insert(vo):
        con = pymysql.connect(host='localhost', port=3306, db='opgg', user='root', password='1234')
        cur = con.cursor(pymysql.cursors.DictCursor)

        sql = 'insert into rank values (%s,%s,%s,%s,%s)'
        result = cur.executemany(sql, vo)

        con.commit()
        con.close()

        print(result, '개 입력 완료')

    def readAll():
        con = pymysql.connect(host='localhost', port=3306, db='opgg', user='root', password='1234')
        cur = con.cursor(pymysql.cursors.DictCursor)

        sql = 'select * from rank'
        cur.execute(sql)

        result = cur.fetchall()

        # print(result)
        # print(type(result))

        # for i in range(0, len(result)):
        #     print(result[i])
        return result

    def read(rank):
        con = pymysql.connect(host='localhost', port=3306, db='opgg', user='root', password='1234')
        cur = con.cursor(pymysql.cursors.DictCursor)

        sql = 'select * from rank where rank=%s'
        cur.execute(sql, rank)

        result = cur.fetchone()

        print(result)
        print(result['name'])

