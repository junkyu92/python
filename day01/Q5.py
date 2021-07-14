s_p = 1000
s_c = 3

b_p = 2500
b_c = 4

price = s_p * s_c + b_p * b_c
dc = price // 10
total = price - dc
print(total)

