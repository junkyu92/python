from DAO import *

id = input('아이디')
pw = input('비밀번호')
name = input('이름')
tel = input('전화번호')

vo = (id, pw, name, tel)

DAO.create(vo)
