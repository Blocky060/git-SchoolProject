import random


def para_func (*para) :
    result = 0
    for I in para :
        result += I
    return result

def dic_func (**para) :   #중요 시험에 나옴
    for k in para.keys() :
        print(k, "-->", para[k], "명입니다.")

def get() :
    return random.randrange(1, 46)
