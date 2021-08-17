#주민등록번호 입력받아서 남자인지 여자인지 구분하는 함수, 나이계산함수 만들어서 출력

def sex(ssn):
    result = "여자"
    if ssn[6] == "1" or ssn[6] == "3":
        result = "남자"
    print(result, "입니다.")

def age(ssn):
    result = 0
    if 22-int(ssn[0:2]) >= 1:
        result = 22-int(ssn[0:2])
    else:
        result = 122-int(ssn[0:2])
    print("나이는 " + str(result) + "살 입니다.")

ssn = input("주민등록번호를 입력하세요.")

sex(ssn)
age(ssn)