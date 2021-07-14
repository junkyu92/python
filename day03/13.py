food = []

while True:
    food.append(input("먹고 싶은 음식 입력(종료: x): "))
    if food[-1] == "x":
        print("-------------------")
        print("입력을 종료합니다.")