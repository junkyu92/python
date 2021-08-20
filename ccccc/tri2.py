# tri2.py
# tri1.py의 triangle클래스를 상속받아 triangle2 클래스 생성 후 check()메서드를 재정의하세요.
# 객체 생성시 정삼각형인지 아닌지를 알려주세요.
# (예: triangle2(60, 60, 60).check() >> 출력: 정삼각형입니다.)
# (예: triangle2(90, 60, 30).check() >> 출력: 정삼각형이 아닙니다.)
# 앞서 tri.py에 실행했던 print 함수들은 tri2.py에서 실행되지 않게 해주세요.

import tri

class triangle2(tri.triangle):
    def check(self):
        result = '정삼각형이 아닙니다.'
        if self.angle1 == self.angle2 == self.angle3 == 60:
            result = '정삼각형입니다'
            tri.triangle.count += 1
        return result

print(triangle2(60, 60, 60).check())
print(triangle2(90, 60, 30).check())
print(triangle2.count)