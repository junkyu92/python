dic = {'1학기': 100, '2학기':50, '3학기':88, '4학기':99}
keys=dic.keys()

for k in keys:
    if dic[k] > 85:
        print(dic[k])

