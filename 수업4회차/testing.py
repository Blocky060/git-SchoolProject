number = int(input("정수 입력> "))
if (number > 0) :
    print("양수입니다")
if (number < 0) :
    print("음수입니다")
if (number == 0) :
    print("0입니다")


import datetime

now = datetime.datetime.now()
month = now.month

if (3 <= month <= 5) :
    print("현재는 봄입니다")
elif (6 <= month <= 8) :
    print("현재는 여름입니다")
elif (9 <= month <= 11) :
    print("현재는 가을니다")
else :
    print("현재는 봄입니다")

x = 10
y = 2
if(x>4):
    if(y>2):
        print(x*y)
else:
    print(x+y)

if (x>10 and x<20):
    print("조건에 맞습니다")