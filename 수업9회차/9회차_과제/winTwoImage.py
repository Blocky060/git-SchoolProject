from tkinter import*

window = Tk()

photo1 = PhotoImage(file="C:\\Users\\Home\\Desktop\\git-SchoolProject\\수업9회차\\qd.gif")
photo2 = PhotoImage(file="C:\\Users\\Home\\Desktop\\git-SchoolProject\\수업9회차\\sd.gif")

lable1 = Label(image=photo1)
lable2 = Label(image=photo2)

lable1.pack(side=LEFT)
lable2.pack()

window.mainloop()