#매게변수 암기
import os
outFp = None
outStr = ""
name = input("파일 이름을 입력해주세요.")
outFp = open("C:\\Users\\Home\\Desktop\\git-SchoolProject\\수업10회차\\%s.txt" % (name), "w", encoding='UTF8')
while True :
    outStr = input("내용 입력 : ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else :
        break
    
outFp.close()
print("정상적으로 파일을 쏨")