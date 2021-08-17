# 양궁, 사격, 펜싱, 태권도, 레슬링 순으로 올림픽 일정이 잡혀 있습니다.
# 위의 일정 순서대로 콘솔에 입력을 받고 (while문 사용)
# 빈 배열에 넣으고 프린트 하시오.
# 역도가 올림픽 종목에 추가되고 일정이 가장 처음으로 배정되어서 배열 제일 첫번째에 역도를 넣으시오. (콘솔 사용 x)

olympic = []
i = 0

while i < 5:
    data = input('종목 입력>> ')
    olympic.append(data)
    i = i + 1

print(olympic)

olympic.insert(0, '역도')
print(olympic)