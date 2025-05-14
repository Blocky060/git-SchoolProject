#매게변수 암기, rb, wb ,43pg
import os
inFp = None
fName, inList, inStr = "", [], ""

fName = input("파일을 입력하세요 : ")

if os.path.exists(fName) :
    inFp = open(fName, "r")

    inList = inFp.readlines()
    for inStr in inList :
        print(inStr, end="")
    inFp.close()
    
else :
    print(fName, "파일이 없습니다.")