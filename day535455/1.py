from tkinter import *

def login():
    id = id_entry.get()
    pw = pw_entry.get()

    print('당신이 입력한 id: ', id)
    print('당신이 입력한 pw: ', pw)

def reset():
    id_entry.delete(0, END)
    pw_entry.delete(0, END)

w = Tk()
w.geometry("500x300")
w.configure(bg = 'lime')

id_label = Label(w, text='id', font=('굴림', 50), width=5)
pw_label = Label(w, text='pw', font=('굴림', 50), width=5)

id_entry = Entry(w, font=('굴림', 50), width=7, bg='yellow')
pw_entry = Entry(w, font=('굴림', 50), width=7, bg='yellow')

button = Button(w, text='로그인',
font=('굴림', 50),
bg='pink',
width=5,
command=login
)
button2 = Button(w, text='지우기',
font=('굴림', 50),
bg='pink',
width=5,
command=reset
)

id_label.grid(row=0, column=0)
id_entry.grid(row=0, column=1)
pw_label.grid(row=1, column=0)
pw_entry.grid(row=1, column=1)
button.grid(row=2, column=1)
button2.grid(row=2, column=0)

w.mainloop()