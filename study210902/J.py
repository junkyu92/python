# 1. 사용자의 입력값 중 숫자만 골라내 그래프를 그려주는 프로그램을 만드세요.
# 예시) 입력>> dig6aa2346dc103bbb05
# 출력)
# *       *
# *       *         *
# *     * *         *
# *   * * *     *   *
# * * * * *     *   *
# * * * * * *   *   *
# 6 2 3 4 6 1 0 3 0 5

a = input("값입력 : ")
b = []
c = []
for i in range(0, len(a)):
    if a[i].isdecimal():
        b.append(int(a[i]))

for i in range(0, max(b)):
    d = []
    for j in range(0, max(b)):
        if b[i] >= max(b)-j:
            d.append("*")
        else:
            d.append(" ")
    c.append(d)

for i in range(0, len(c)):
    print(c[i])
print(b)