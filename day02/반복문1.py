target = 55
cnt = 0
while True:
    user = int(input('숫자를 입력하세요.>> '))
    cnt = cnt+1
    if user == target:
        print("정답입니다.")
        print(cnt)
        break
    elif user > target:
        print("너무 큽니다.")
    elif user < target:
        print("너무 작습니다.")

