# 1) 중간고사의 등수가 1등 이순신, 2등 권율, 3등 유성룡 , 4등 원균으로 발표되었다.
# 하지만 4등 원균이 전학을 가서 3등까지만 집계가 되었다.
# 최초 중간고사 1등부터 4등까지 프린트, 원균이 전학간 후 1등부터 4등까지 프린트, 그리고 2등이 누군지 '중간고사 2등은 xx'의 형식으로 프린트하시오
# -----------------------------------------------------------------

list = ["이순신", "권율", "유성룡", "원균"]
print(list)
list.remove("원균")
print(list)
print("중간고사 2등은 " + list[1])

# 2)'주민등록번호를 숫자만 띄어쓰기 없이 13자리를 입력하세요. 종료)x>> '를 출력하고 콘솔에서 입력을 받아서 탄생연도를 이용하여 맞을 백신을 띄우시오.
# 92년생 이상, 또는 03년생 이하는 화이자
# 81년생부터 91년생은 얀센
# 70년생부터 80년생은 아스트라제네카
# 61년생부터 69년생은 모더나
# 10년생부터 60년생은 화이자
# 그외엔 '대상자가 아닙니다.' 출력
# *while문을 이용하시오.


while True:
    ssn = input("주민번호를 입력하세요 종료)x>> ")
    if ssn == "x":
        print("종료합니다.")
        break
    if int(ssn[0:2]) >= 92 or int(ssn[0:2]) <= 3:
        print("화이자")
    elif 81 <= int(ssn[0:2]) <= 91:
        print("얀센")
    elif 70 <= int(ssn[0:2]) <= 80:
        print("아스트라제네카")
    elif 61 <= int(ssn[0:2]) <= 69:
        print("모더나")
    elif 10 <= int(ssn[0:2]) <= 60:
        print("화이자")
    else:
        print("대상자가 아닙니다.")