# a = 'select name from member where id = python'
# 1. 첫 단어를 검색하여 crud중 어떤기능을 하는 sql문인지 출력한다.
#
# 2. sql문 a에서 name에 해당하는 부분을 target
#            member에 해당하는 부분을 table
#            python에 해당하는 부분을 id로 그루핑하고
#   a가 어떤 기능을 하는 sql문인지 자세히 출력한다.


import re

a = 'select name from member where id = python'

p = re.compile("\w+")
m = p.match(a)

result = "sql문이 아닙니다"
if m.group() == "insert":
    result="create기능"
    print(result)
elif m.group() == "select":
    result = "read기능"
    print(result)
    p = re.compile(r"select+\s+(?P<target>.+)\s+from+\s+(?P<table>.+)\s+where+\sid+\s+=+\s(?P<id>.+)")
    m = p.search(a)
    print(m.group("table") + " table에서 아이디가 " + m.group("id") + "인 회원의 " + m.group("target") + "을 검색한다.")
elif m.group() == "update":
    result = "update기능"
    print(result)
elif m.group() == "delete":
    result = "delete기능"
    print(result)


