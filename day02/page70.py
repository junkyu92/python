price = int(input("물건값: "))
cash = int(input("받은돈: "))

change = cash - price

change1 = change // 10000
change2 = change % 10000 // 5000
change3 = change % 5000 // 1000

print("10000원권: ", change1)
print("5000원권: ", change2)
print("1000원권: ", change3)

