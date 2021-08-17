#id와 pw가 각각 root/1234일 경우 로그인하는 함수를 만들고 id,pw입력받아서 함수사용하여 로그인 성공/실패
def login(id, pw):
    result = "로그인 실패"
    if id == "root" and pw == "1234":
        result = "로그인 성공"
    print(result)

id = input("id입력: ")
pw = input("pw입력: ")

login(id, pw)




# 메인 => 회원가입
# 메인 => 로그인
# 메인 => 회원정보(수정,탈퇴)
#
# 메인 => 지도 => 숙소
#
# 메인 => 숙소 => 장바구니 => 예약 => 결제
# 메인 => 결제확인
#
# 메인 => 게시판
