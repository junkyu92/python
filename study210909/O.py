# age_list를 정규식을 통해 하기 딕셔너리 내용으로 출력되게 만들어보세요
# 출력 내용 => {'Janice': '22', 'Theon': '33', 'Gabriel': '44', 'Joey': '21'}

import re

age_list = '''
Janice is 22 and Theon is 33
Gabriel is 44 and Joey is 21
'''
p = re.compile('(?P<name>\S+)\s+is\s+(?P<age>\S+)')
r = p.findall(age_list)

result = {}
for i in r:
    result[i[0]] = i[1]

print(result)