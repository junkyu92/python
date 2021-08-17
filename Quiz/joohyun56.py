#사칙연산 계산기를 만들어보자
#1) 사칙연산 진행이 가능한 계산기 클래스 생성
# a = Calculator()
# print(a.add(3,4)) #7
# print(a.sub(3,4)) #-1
# print(a.mul(3,4)) #12
# print(a.div(3,3)) #1.0
#2) 계산기 사용 횟수를 출력하는 별도의 함수 생성
# count(a)          #계산기의 사용 횟수는 4회 입니다.

class Calculator:
    count = 0
    def add(self, x, y):
        result = x+y
        self.count += 1
        return result

    def sub(self, x,y):
        result = x-y
        self.count += 1
        return result

    def mul(self, x,y):
        result = x*y
        self.count += 1
        return result

    def div(self, x,y):
        result = x/y
        self.count += 1
        return result

    def cnt(self):
        print(self.count)

a = Calculator
print(a.add(3,4)) #7
print(a.sub(3,4)) #-1
print(a.mul(3,4)) #12
print(a.div(3,3)) #1.0

print(a.cnt())