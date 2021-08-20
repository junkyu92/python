# class Person을 생성하고 이름과 주민 번호를 변수로 가지도록 정의하시오.
# Class Ceo를 생성하고 연봉을 변수로 추가해서 가지도록 정의하시오.
# CEO인 홍길동의 주민번호 앞자리는 901112이고 봉급은 천만원으로 해서 프린트하시오.

class Person:
    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn


class Ceo(Person):
    def __init__(self, name, ssn, salary):
        super().__init__(name, ssn)
        self.salary = salary

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setSsn(self, ssn):
        self.ssn = ssn

    def getSsn(self):
        return self.ssn

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary


ceo = Ceo("홍길동", "901112", "천만원")
print("이름: " + ceo.getName() + ", 생년월일: " + ceo.getSsn() + ", 봉급: " + ceo.getSalary())