a = []
for i in range(0, 5):
    a.append(input("장소: "))

print("--------------")
print(a)

a.remove("강남")
print(a)

for i in range(0, len(a)):
    if a[i] == "제주도":
        a[i] = "제주시"
print(a)

for i in  range(0, len(a)):
    print(str(i + 1) + "위: " + a[i])