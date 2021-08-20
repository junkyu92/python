# 1. 연락처 관리 프로그램 UI
#    1. 친구 리스트 출력
#    2. 친구 추가
#    3. 친구 삭제
#    4. 이름 변경
#    9. 종료
#    메뉴를 선택하세요 >>
#   -------------------------
# 2. 친구를 추가하시고 출력하세요. => 홍길동, 임길동
# 3. 친구 이름을 변경하시고 출력하세요. => 임길동 -> 임꺽정
# 4. 친구를 삭제하시고 출력하세요 => 홍길동
# 5. 마지막에 시스템을 종료하세요.
list = []
while True:
    print("1. 친구 리스트 출력")
    print("2. 친구 추가")
    print("3. 친구 삭제")
    print("4. 이름 변경")
    print("9. 종료")
    c = int(input("메뉴를 선택하세요 >> "))
    print("--------------------")

    if c == 9:
        break
    elif c == 2:
        n = input("추가할 친구를 입력해주세요 >> ")
        list.append(n)
    elif c == 3:
        n = input("삭제할 친구를 입력해주세요 >> ")
        list.remove(n)
    elif c == 1:
        print(list)
    elif c == 4:
        n1 = input("어떤 친구를 변경할지 써라 >> ")
        n2 = input("뭘로 변경할지 >> ")
        for i in range(0, len(list)):
            if list[i] == n1:
                list[i] = n2

