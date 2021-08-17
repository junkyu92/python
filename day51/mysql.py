import pymysql


def create(datas):
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor(pymysql.cursors.DictCursor)
    print(cur)

    sql = 'insert into member values(%s, %s, %s, %s)'

    result = cur.execute(sql,datas)
    print('처리결과', result, '개')

    con.commit()
    con.close()

vo = ('test1', 'test1', 'test1', 'test1')
create(vo)
