answer_how_calculate = input("1. 입력한 수식 계산  2. 두 수 사이의 합계 : ")
if (answer_how_calculate == '1') :
    calculate = input("*** 수식을 입력하세요 : ")
    print(calculate, "결과는",  eval(calculate))
elif (answer_how_calculate == '2') :
    first_num = int(input("첫 번째 숫자를 입력해주세요 : "))
    second_num = int(input("첫 번째 숫자를 입력해주세요 : "))
    result = 0
    for I in range (first_num, second_num+1):
        result = I + result
    print(first_num,"+...+",second_num,"는", result,"입니다.")
        
else :
    print("1 혹은 2만 입력해야 합니다")