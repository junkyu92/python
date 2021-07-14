score1 = int(input("중간고사 점수: "))
score2 = int(input("기말고사 점수: "))

result1 = score1 * 0.4 + score2 * 0.6

if result1 >= 60:
    print("교양음악의 최종학점은 pass입니다.")
else:
    print("교양음악의 최종학점은 fail입니다.")
print("**************")

score2_1 = int(input("중간고사 점수:"))
score2_2 = int(input("기말고사 점수:"))

result2 = score2_1 * 0.4 + score2_2 * 0.6

if result2 >= 60:
    print("교양음악의 최종학점은 pass입니다.")
else:
    print("교양음악의 최종학점은 fail입니다.")