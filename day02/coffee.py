coffee_price = int(input("커피값: "))
count = int(input("인원: "))
total = coffee_price * count

if coffee_price >= 10000:
    print(total - 2000, "원 지불")
else:
    print(total, "원 지불")
