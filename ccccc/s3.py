# 이름과 나이를 속성으로 가진 강아지 클래스를 정의하라.
# 그리고 이름이 바둑이, 나이가 5살인 객체와 이름이 멍멍이, 나이가 7살인 객체를 생성하고 나이를 출력하시오.

class Dog:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

d = Dog("바둑이", 5)
d2 = Dog("멍멍이", 7)

print(d.age)
print(d2.age)
