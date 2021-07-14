a = []
for i in range(0, 3):
    a.append(int(input("학기 총점: ")))

total = 0
for i in range(0, len(a)):
    total = total + a[i]
avg = total / len(a)

print("-------------------")
print("총학기 평균은 " + str(avg) + "점입니다.")