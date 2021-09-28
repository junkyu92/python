#간단한 타자연습 프로그램 만들기
#진행할 짧은 글 연습 개수를 입력받아, 해당하는 만큼의 연습을 진행하고
#정확도(소수점 없는 백분율)와 걸린시간(초)를 출력하는 프로그램(함수) typing_game을 만들어보세요
#연습 개수의 경우 사용자가 정수만 입력한다고 가정합니다
#연습 문장은 제시된 리스트에서 랜덤으로 나오도록 해주세요
import math
import time
import random
sentences = ['String sql = "select * from member";',
             '@Controller',
             '@Autowired',
             '@RequestMapping()',
             '@Repository',
             'static SingleObject object;',
             'public static SingleObject getInstance()',
             'Connection con = DriverManager.getConnection(url, user, password);',
             'Class.forName("com.mysql.jdbc.Driver");',
             'PreparedStatement ps = con.prepareStatement(sql);']

def typing_game(n):
    for j in range(0, n):
        a = random.choice(sentences)
        start = time.time()
        b = input(a + "\n")
        cnt = 0
        for i in range(0, len(a)):
            try:
                if a[i] == b[i]:
                    cnt = cnt + 1
            except:
                cnt = cnt
        result = int(cnt / len(a) * 100)
        print("당신의 정확도는 " + str(result) + "%입니다.")
        print("걸린 시간은 총 ", math.floor(time.time() - start), "초입니다.\n")
#실행문장
print("타자 연습에 오신 것을 환영합니다")
n = int(input("몇 줄의 짧은 글 연습을 하시겠어요?(1 이상의 정수) >> "))
typing_game(n)