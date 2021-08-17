# 1) 다음 문장의 글자를 거꾸로 출력해보세요 (문자열 인덱싱과 for문 이용)
# "Welcome to Python World!"
# => (출력내용) "!dlroW nohtyP ot emocleW"

text = "Welcome to Python World!"
new = ""
for i in range(1, len(text) + 1):
    print(text[-i], end="")
print("")

for i in range(1, len(text) + 1):
    new = new + text[-i]
print(new)


