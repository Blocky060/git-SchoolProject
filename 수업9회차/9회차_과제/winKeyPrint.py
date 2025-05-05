from tkinter import*
from tkinter import messagebox


def UpkeyEvent(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키 : shift + 위쪽 화살표")

def DownkeyEvent(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키 : shift + 아래쪽 화살표")

def RightkeyEvent(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키 : shift + 오른쪽 화살표")

def LeftkeyEvent(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키 : shift + 왼쪽 화살표")



window = Tk()

window.bind("<Shift-Up>", UpkeyEvent)
window.bind("<Shift-Down>", DownkeyEvent)
window.bind("<Shift-Right>", RightkeyEvent)
window.bind("<Shift-Left>", LeftkeyEvent)

window.mainloop()

