# 정규식을 사용하여 80년도생, 90년도생, 남자, 여자가 각각 몇 명인지 구해보세요
import re

string2 = """
950825-1234567
850612-2987654
930525-2876552
940808-2394945
841019-1102913
870718-1203913
910803-2113709
871001-1987121
951203-1655786
931213-1861930
900312-2908133
871032-1543922
911213-2877651
"""

# 정규식을 사용해 이메일만 골라내서 하나씩 프린트해보세요
string = """
purple smurf667@aol.com, send a message bill@billwaldon.com dishwasher blah
rem54mdds@sbcglobal.net monkey banana peel tommfs1982@hotmail.com
kakao switch christina-alvarez@gmail.net nintendo sony playstation
verdun.singh@stanford.edu university thomas tammy@reallybigknockers.net
disney netflix wavve donkey alexander@null.net pikachu pokemon
"""

p = re.compile('^8+', re.M)
r = p.findall(string2)
print("80년도생 " + str(len(r)) + "명")

p = re.compile('^9+', re.M)
r = p.findall(string2)
print("90년도생 " + str(len(r)) + "명")

p = re.compile('-1', re.M)
r = p.findall(string2)
print("남자 " + str(len(r)) + "명")

p = re.compile('-2', re.M)
r = p.findall(string2)
print("여자 " + str(len(r)) + "명")

p = re.compile('\S+@\S+')
r = p.findall(string)

for i in r:
    print(i)