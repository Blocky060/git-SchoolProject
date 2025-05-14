#매게변수 암기
import os
inFp, outFp = None, None
inStr = ""
inFp = open(input("소스 파일 입력 : "), "r", encoding='UTF8')
outFp = open(input("타깃 파일 입력 : "),"w", encoding='UTF8')


inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

outFp.close()
inFp.close()
print("정상적으로 파일을 쏨")