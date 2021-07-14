target = 55
cnt = 0

while True:
    a = int(input("숫자입력: "))
    cnt = cnt + 1
    if a == 55:
        print("정답.")
        break
    elif a > 55:
        print("너무 큽니다.")
    else:
        print("너무 작습니다.")
print(cnt, "번만에 맞춤.")