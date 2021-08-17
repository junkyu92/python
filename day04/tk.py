from tkinter import *
from tkinter import messagebox

def login():
    id2 = id_entry.get()
    print('입력한 ID는 ', id2)
    pw2 = pw_entry.get()
    print('입력한 PW는 ', pw2)

    if id2 == 'root' and pw2 == '1234':
        messagebox.showinfo('로그인성공', '축하합니다')
        print('로그인성공')
    else:
        messagebox.showinfo('로그인실패', '다시 해보세요')
        print('로그인실패')

w = Tk()
w.geometry("500x250")

id = Label(w, text='ID입력', font=('궁서', 30))
id.pack()

id_entry = Entry(w, font=('궁서', 30), bg='blue', fg='white')
id_entry.pack()

pw = Label(w, text='PW입력', font=('궁서', 30))
pw.pack()

pw_entry = Entry(w, font=('궁서', 30), bg='blue', fg='white')
pw_entry.pack()

b = Button(w,
           text='로그인 처리',
           font=('궁서', 30),
           bg='yellow',
           command=login
           )
b.pack()

w.mainloop()