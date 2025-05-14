#매게변수 암기
import os
inFp, outFp = None, None
inStr = ""

outFp = open("C:\\Users\\Home\\Desktop\\git-SchoolProject\\수업10회차\\data2.txt", "w", encoding='UTF8')
inFp = open("C:\\Users\\Home\\Desktop\\git-SchoolProject\\수업10회차\\data.txt", "r", encoding='UTF8')

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

outFp.close()
inFp.close()
print("정상적으로 파일을 쏨")