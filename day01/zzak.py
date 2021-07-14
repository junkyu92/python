name = input("당신의 짝이름을 입력하세요: ")
interest = input("짝의 관심사를 입력하세요: ")

import tkinter.messagebox

tkinter.messagebox.showinfo(name, interest)

if interest == "파이썬":
    print("프로그래머가 되실거군요")
else:
    print("데이터분석가가 되실거군요")

