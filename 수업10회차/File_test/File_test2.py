# "C:\Users\Home\Desktop\git-SchoolProject\수업10회차\File_test\CookBook 파이썬을 공부합니다..txt"

inFp = None
inStr=""

inFp = open("C:\\Users\\Home\\Desktop\\git-SchoolProject\\수업10회차\\File_test\\CookBook 파이썬을 공부합니다..txt", "r", encoding='UTF8')


while True :
    
    inStr = inFp.readline()
    if (inStr == ""):
        break
    print(inStr, end="")
    
inFp.close()