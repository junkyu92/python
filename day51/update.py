from DAO import *

id = input('아이디')
pw = input('비밀번호')

vo = (pw, id)

DAO.update(vo)