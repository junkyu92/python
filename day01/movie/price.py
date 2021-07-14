def info():
    name = input("같이 볼사람: ")
    relationship = input("관계: ")
    print(name, ",", relationship)

def pay():
    price = 10000
    count = int(input("인원수: "))
    total = price * count
    print("총 지불금액", total)
