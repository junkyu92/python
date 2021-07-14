coffee_price = int(input("커피값 입력: "))
coffee_count = int(input("커피 인원수: "))
sum = coffee_price * coffee_count

if sum >= 20000:
    print("2000원을 할인해드립니다.")
    print("할인된 금액 ", sum - 2000)
else:
    print("계산값을 다 지불하셔야 합니다.")
    print(sum)
