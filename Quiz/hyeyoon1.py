# 1) 자동차 검사
# 안전성 점수 (30%) : 100
# 속도 점수 (50%) : 80
# 연비 점수 (20%) : 60
# (출력내용) 82점 우수입니다
# (90점 이상: 최우수, 80점 이상: 우수, 70점 이상: 보통, 그것도 아니면: 미달)

score1 = int(input("안전성 점수 (30%) : "))
score2 = int(input("속도 점수 (50%) : "))
score3 = int(input("연비 점수 (20%) : "))

r1 = score1 * 0.3
r2 = score2 * 0.5
r3 = score3 * 0.2

score = r1+r2+r3
result = "미달"
if score >= 90:
    result = "최우수"
elif score >= 80:
    result = "우수"
elif score >= 70:
    result = "보통"
print(str(int(score)) + "점 " + result + "입니다.")