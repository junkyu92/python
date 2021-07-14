food = []

for i in range(0, 3):
    fi = input("음식을 입력하세요.")
    food.append(fi)

print(food[1])
print(food[0:2])
print(food[1:])
food[0] = "라면"
print(food[0])
