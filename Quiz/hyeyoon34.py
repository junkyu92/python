# 오늘 일기를 open함수를 이용하여 txt 파일로 저장해 보세요.
# 파일 이름: 20210729.txt
# 내용: 나는 오늘 라면이 먹고 싶었지만 집에는 라면이 없었다.
# 그래서 편의점을 갔는데 진라면이 1+1이라 진라면을 샀다.
# 집 가는 길에 떡볶이 가게 앞을 지나가는데 떡볶이 냄새가 났다.
# 오늘 저녁은 떡볶이를 시켜 먹어야겠다.
with open("20210729.txt", 'w', encoding='utf-8') as f:
    f.write("나는 오늘 라면이 먹고 싶었지만 집에는 라면이 없었다.\n")
    f.write("그래서 편의점을 갔는데 진라면이 1+1이라 진라면을 샀다.\n")
    f.write("집 가는 길에 떡볶이 가게 앞을 지나가는데 떡볶이 냄새가 났다.\n")
    f.write("오늘 저녁은 떡볶이를 시켜 먹어야겠다.\n")

# 1. '떡볶이'와 '라면' 단어를 일기에 각각 몇 번 썼는지 구해보세요.
ra = 0
dd = 0
with open("20210729.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        dd += line.count('떡볶이')
        ra += line.count('라면')
print('라면은', ra, '번, 떡볶이는', dd, '번')

# 2. 일기 속 단어를 바꾸는 함수 edit()을 만들어서
#   라면을 비빔면으로, 떡볶이를 차돌박이로 바꿔 보세요.
#   1) edit(입력값: 파일이름, 바꾸고 싶은 단어, 바꿀 단어)
#      예: edit("20210729.txt", '라면', '비빔면')
#      예: edit("20210729.txt", '떡볶이', '차돌박이')
#   2) 잘 바뀌어서 저장됐는지 txt파일을 열어 확인해 보세요.
def edit(a, b, c):
    line1 = ''
    with open(a, 'r', encoding='utf-8') as f1:
        while True:
            line2 = f1.readline()
            line1 += line2.replace(b, c)
            if not line2: break
    with open(a, 'w', encoding='utf-8') as f2:
        f2.write(line1)
edit("20210729.txt", '라면', '비빔면')
edit("20210729.txt", '떡볶이', '차돌박이')