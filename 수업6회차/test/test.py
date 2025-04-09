#test
print("testing")

def get_shop_name() :
    return ("커피장인")

def get_branch_name() :
    return ("여의도 본점")

def print_name() :
    print(get_shop_name())
    print(get_branch_name())

print_name()

a = [1, 2, 3]
a.insert(1, 4)
print(a)

order_detail = []

def make_order (name, qty) :
    order_detail.append({"이름" : name, "수량" : qty})

print(order_detail)
make_order("아메리카노", 2)
make_order("카페라떼", 4)
print(order_detail)                                                                                                                                                                                                                                                                                                                                                                                                                                               

#빈칸채우기, 결과예상, 코드체우기 등 / 12시 10분