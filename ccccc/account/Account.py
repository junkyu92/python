# 1) Account 클래스 생성
# > 입력값을 이름(str), 계좌번호(str), 금액(int)으로 한 생성자를 만드세요
# 2) Account 클래스를 상속받는 자식 클래스 2개 생성
# > AccountNormal
#    - 클래스 변수 (상수) RATE (double, 0.01)
#    - 총 보유 금액 출력 메서드 (금액 * rate)
# > AccountVip
#    - 클래스 변수 (상수) RATE (double, 0.1)
#    - 총 보유 금액 출력 메서드 (금액 * rate)
# 3) Account.py 파일을 실행하면 하기 파일이 출력되도록 하자
# "이 파일은 모듈입니다. 다른 파일에서 import하여 사용해주세요"
# (import하여 사용 시 위의 문구는 출력되지 않는다)
# [실행파일]
# 4) 다른 파이썬 파일에서 Account.py를 import해 AccountNormal과 AccountVip 객체를 하나씩 만들고, 메서드를 사용해 총 보유 금액을 각각 출력해보세요

class Account:
    name = ""
    num = ""
    money = 0

    def __init__(self, name, num, money):
        self.name = name
        self.num = num
        self.money = money


class AccountNormal(Account):
    rate = 0.01

    def total(self):
        print(self.money + self.money * self.rate, "원")


class AccountVip(Account):
    rate = 0.1

    def total(self):
        print(self.money + self.money * self.rate, "원")


if __name__ == "__main__":
    print("이 파일은 모듈입니다. 다른 파일에서 import하여 사용해주세요")



