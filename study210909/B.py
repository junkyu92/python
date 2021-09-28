# 아이디 유효성 검사
# 영문과 숫자만으로 아이디를 입력하는데 5자 미만이거나 16자 초과인 경우 "유효하지 않은 아이디입니다." 출력
# 5자 이상 15자 이하인 경우 "유효한 아이디입니다." 출력
# "헬로 World"에서 영어를 *로 변환하고,
# 다음에 한글을 *로 변환하라.
import re

a = input("영문과 숫자만으로 아이디 입력")
result = "유효한 아이디입니다."

if len(a) < 5 or len(a) > 16:
    result = "유효하지 않은 아이디입니다."
    print(result)


def change(match):
    result = len(r.group()) * "*"
    return result


q = "헬로 World"
p = re.compile('[a-z+]', re.I)
r = p.search(q)
print(p.sub(change, q))

p = re.compile('[ㄱ-ㅣ가-힣+]')

r = p.search(q)
print(p.sub(change, q))