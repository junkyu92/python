class A:
    product = ""
    name = ""
    money = 0

    def __init__(self, product, name, money):
        self.product = product
        self.name = name
        self.money = money

    def p(self):
        return self.product + ' 통장에는 ' + str(self.money) + '만원이 들어있어요.'


    def n(self):
        return self.name + '의 통장에는' + str(self.money) + '만원이 들어있어요.'


if __name__ == '__main__':
    a1 = A('청약저축', '김아무개', 500)
    a2 = A('내비상금', '김아무개딸', 30)
    a3 = A('자유적금', '박아무개', 100)

    print(a2.p())
    print(a3.n())

    print('우리 집 전체 예금액은 ' + str(a1.money+a2.money+a3.money) + '만원 이에요!')