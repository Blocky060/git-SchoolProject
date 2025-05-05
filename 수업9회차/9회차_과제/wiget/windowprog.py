from tkinter import*
from time import*

frameList = ["1.gif","2.gif", "3.gif", "4.gif", "5.gif", "6.gif", "7.gif", "8.gif", "9.gif"]
photoList = [None]*9
num = 0

def clickNext():
    global num
    num += 1
    if (num > 8):
        num = 0
    photo = PhotoImage(file="C:\\Users\\Home\\Desktop\\git-SchoolProject\\수업9회차\\9회차_과제\\wiget\\image\\"+frameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    title.configure(text=frameList[num])

def clickPrev():
    global num
    num -= 1
    if (num < 0):
        num = 8
    photo = PhotoImage(file="C:\\Users\\Home\\Desktop\\git-SchoolProject\\수업9회차\\9회차_과제\\wiget\\image\\"+frameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    title.configure(text=frameList[num])

window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(text = "<< 이전", command=clickPrev)
btnNext = Button(text = ">> 다음", command=clickNext)



photo = PhotoImage(file="C:\\Users\\Home\\Desktop\\git-SchoolProject\\수업9회차\\9회차_과제\\wiget\\image\\"+frameList[0])
pLabel = Label(image = photo)
title = Label(text=frameList[0])

btnNext.place(x = 400, y = 10)
btnPrev.place(x = 250, y = 10)

title.place(x = 325, y = 10)

pLabel.place(x=15, y = 50)


window.mainloop()