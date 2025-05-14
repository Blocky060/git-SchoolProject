from tkinter import *

def loadImage(fName):
    global inImage, XSIZE, YSIZE
    fp = open(fName, 'rb')
    inImage = []
    for i in range(YSIZE):
        tmpList = []
        for k in range(XSIZE):
            data = int.from_bytes(fp.read(1), 'big')
            tmpList.append(data)
        inImage.append(tmpList)
    fp.close()

def displayImage(image):
    global XSIZE, YSIZE, paper
    for i in range(YSIZE):
        for k in range(XSIZE):
            data = image[i][k]
            hexColor = "#%02x%02x%02x" % (data, data, data)
            paper.put(hexColor, (k, i))

window = Tk()
window.title("흑백 사진보기")
XSIZE, YSIZE = 256, 256
canvas = Canvas(window, width=XSIZE, height=YSIZE)
canvas.pack()

paper = PhotoImage(width=XSIZE, height=YSIZE)
canvas.create_image((XSIZE / 2, YSIZE / 2), image=paper, state="normal")

filename = "C:\\Users\\Home\\Desktop\\git-SchoolProject\\수업10회차\\Lenna.raw"
loadImage(filename)
displayImage(inImage)

window.mainloop()
