# "textfile.txt"의 파일명으로 "글자를 파일에 쓰세요"라고 저장하고,
# 발생할 수 있는 IOError를 예외처리 후에 "파일을 찾을 수 없습니다."라고 출력하시오.
# 만약 예외가 발생하지 않는다면 "파일을 생성했습니다." 라고 출력하시오.

# 가위바위보 게임 만들기
# random 모듈을 사용해 베타고라는 가위바위보 게임을 만들어 보세요.
try:
    f = open("textfile.txt", "w", encoding="UTF-8")
    f.write("글자를 파일에 쓰세요")
    f.close()
    print("파일을 생성했습니다.")
except FileNotFoundError:
    print("파일을 찾울 수 없습니다.")


import random

a = int(input("가위 바위 보 (0, 1, 2) >> "))
x = random.randint(0, 3)
result = "이김"
if a == 0:
    if x == 0:
        result = "비김"
    elif x == 1:
        result = "짐"
elif a == 1:
    if x == 1:
        result = "비김"
    elif x == 2:
        result = "짐"
elif a == 2:
    if x == 2:
        result = "비김"
    elif x == 0:
        result = "짐"
else:
    result = "잘못 입력하셨습니다."

print(result)

