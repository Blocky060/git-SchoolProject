from tkinter import*
from tkinter import messagebox

def myFunc():
    messagebox.showinfo("강아지 버튼", "강아지가 귀엽죠?")

window = Tk()

photo1 = PhotoImage(file="C:\\Users\\Home\\Desktop\\git-SchoolProject\\수업9회차\\qd.gif")

button = Button(image=photo1, command=myFunc)

button.pack()


window.mainloop()