# tri.py
# triangle이라는 클래스를 만들어 객체 생성 후
# 메서드를 이용하여 삼각형인지 아닌지, 총 몇 개의 삼각형이 만들어졌는지 알려주세요.
# (예: triangle(90, 30, 60).check() >> 출력: 삼각형입니다.)
# (예: triangle(90, 90, 30).check() >> 출력: 삼각형이 아닙니다.)
# (예: triangle.count >> 1)

class triangle:
    count = 0
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check(self):
        result = '삼각형이 아닙니다'
        if self.angle1 + self.angle2 + self.angle3 == 180:
            result = '삼각형입니다'
            triangle.count += 1
        return result

if __name__ == "__main__":
    print(triangle(90, 30, 60).check())
    print(triangle(90, 90, 30).check())
    print(triangle.count)