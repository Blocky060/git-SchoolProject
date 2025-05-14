inFp, outFp = None, None
inStr, outStr = "", ""
i = 0
secu = 0



secuYN = input("1. 암호화, 2. 복호와 중 선택 : ")
inFname = input("입력 파일명 : ")
outFname = input("출력 파일명 : ")

if secuYN == "1" :
    secu = 100
else :
    secu = -100
    
    
inFp = open(inFname, 'r', encoding='UTF8')
outFp = open(inFname, 'w', encoding='UTF8')

while True :
    inStr = inFp.readlines()
    if not inStr :
        break
    outStr = ""
    for i in range(0, len(inStr)) :
        ch = inStr[i]
        chNum = ord(ch)
        chNum += secu
        ch2 = chr(chNum)
        outStr += ch2
        
    outFp.write(outStr + ch2)
    
outFp.close()
inFp.close()
print("완료",inFname, "", outFname)

#C:\\Users\\Home\\Desktop\\git-SchoolProject\\수업10회차\\normal.txt