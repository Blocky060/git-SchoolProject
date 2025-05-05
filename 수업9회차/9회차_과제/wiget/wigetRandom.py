from tkinter import*
from random import*

btnList = [None]*9
frameList = ["1.gif","2.gif", "3.gif", "4.gif", "5.gif", "6.gif", "7.gif", "8.gif", "9.gif"]
photoList = [None]*9
i,k=0,0
xpos,ypos=0, 0
num = 0

window = Tk()
window.geometry("210x210")

shuffle(frameList)

for i in range(9):
    photoList[i] = PhotoImage(file="C:\\Users\\Home\\Desktop\\git-SchoolProject\\수업9회차\\9회차_과제\\wiget\\image\\"+frameList[i])
    btnList[i] = Button(image=photoList[i])

for i in range(3):
    for k in range(3):
        btnList[num].place(x=xpos, y=ypos)
        num += 1
        xpos+=500
    xpos=0
    ypos+=500

window.mainloop()