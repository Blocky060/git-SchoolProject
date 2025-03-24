HowPrint = int(input("입력 진수 결정 (16/10/8/2) : "))
Number = input("값 입력 : ")

Number10 = int(Number, HowPrint)


print ("16진수 ==> ", hex(Number10))
print ("10진수 ==> ", Number10)
print ("8진수 ==> ", oct(Number10))
print ("2진수 ==> ", bin(Number10))