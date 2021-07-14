start = int(input("시작값을 입력하세요."))
end = int(input("끝값을 입력하세요."))

cnt = end - start - 1
sum = 0
for i in range(start+1, end):
    sum = sum + i

avg = sum/cnt

print(cnt)
print(sum)
print(avg)