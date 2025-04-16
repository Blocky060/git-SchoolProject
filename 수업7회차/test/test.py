from test_def import*


hap = para_func(10, 20, 30)
print(hap)


dic_func(트와이스 = 9, 소녀시대 = 7, 걸스데이 = 4, 블랙핑크 = 4)


lotto = []
num = 0
print("** 로또 추첨을 시작합니다. **\n")

while True :
    num = get()
    if (lotto.count(num) == 0) :
        lotto.append(num)
    if (len(lotto) >= 6) :
        break
print("추첨된 로또 번호 ==> ", end = '')
lotto.sort() 
for i in range(6) :
    print("%d " %lotto[i],end = '')


