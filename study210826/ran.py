# 리스트넣어서 랜덤추첨하는 함수 만들기 (중복x)
# member = ["이준규", "변승원", "오주현", "전혜윤"]
# print(ran(member, 2))
#
# => ['변승원', '전혜윤']


import random


def ran(member, j):
    mem = []
    for i in range(j):
        a = random.choice(member)
        member.remove(a)
        mem.append(a)
    return mem


member = ["이준규", "변승원", "오주현", "전혜윤"]
print(ran(member, 2))

