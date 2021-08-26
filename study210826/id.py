# 계산기 만들기 , 나누기0 입력시 예외처리(ZeroDivisionError)
#
# class Calculator:
#     def __init__(self):
#         self.result = 0
#
#     def plus(self, x):
#         self.result += x


class Calculator:
    def __init__(self):
        self.result = 0

    def plus(self, x):
        self.result += x

    def minus(self, x):
        self.result -= x

    def multiply(self, x):
        self.result *= x

    def division(self, x):
        try:
            self.result /= x
        except ZeroDivisionError:
            print("0으로는 나눌 수 없습니다.")


a = Calculator()
a.plus(4)
a.minus(2)
a.multiply(3)
a.division(0)
a.division(2)
print(a.result)
