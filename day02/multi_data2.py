hobby = []
hobby.append('코딩')
print("개수>> ", len(hobby))
hobby.append('등산')
print("개수>> ", len(hobby))


for _ in range(3):
    data = input('당신의 새로운 취미는?>> ')
    hobby.append(data)

print("개수>> ", len(hobby))

for i in hobby:
    print(i, end=' ')

