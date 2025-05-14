# "C:\Users\Home\Desktop\git-SchoolProject\수업10회차\File_test\CookBook 파이썬을 공부합니다..txt"

inFp = None
inStr=""
inList = []

inFp = open("C:\\Users\\Home\\Desktop\\git-SchoolProject\\수업10회차\\File_test\\CookBook 파이썬을 공부합니다..txt", "r", encoding='UTF8')


inList = inFp.readlines()
for inStr in inList:
    print(inStr, end="")
    
inFp.close()