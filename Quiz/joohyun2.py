# 2) 다음 딕셔너리에서 value값이 0인 key의 집합(리스트)을 만들어 출력하시오
# dic = {'a':0, 'b':0,'c':2,'d':1,'e':0}
# => (출력내용) ['a','b','e']

dic = {'a':0, 'b':0,'c':2,'d':1,'e':0}
dic2 = {}

keys = dic.keys()
for k in keys:
    if dic[k] == 0:
        print(k, end="")
print()

for k in keys:
    if dic[k] == 0:
        dic2[k] = dic[k]

print(dic2)
print(list(dic2))