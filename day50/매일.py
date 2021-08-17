class Day:
    work1 = ""
    hour1 = 0
    place1 = ""

    def __init__(self, work1, hour1, place1):
        self.work1 = work1
        self.hour1 = hour1
        self.place1 = place1

    def study(self):
        return self.work1 + "를 " + str(self.hour1) + "시간하다"

    def where(self):
        return self.place1 + '에서 ' + self.work1 + '를 하다'

    def __str__(self):
        return 'class Day의 속성값들>> ' + self.work1 + "," + str(self.hour1) + ',' + self.place1

if __name__ == '__main__':
    day1 = Day('파이썬공부', 10, '강남')
    day2 = Day('자바공부', 11, '신촌')
    day3 = Day('db공부', 12, '종로')

    print(day1)
    x = day1.where()
    print(x)

    print(day1.study())