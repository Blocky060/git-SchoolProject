class car :   #현실세계의 사물을 컴퓨터 안에서 구현할려고 고안한 개념 (field) (자용차의 기능은 함수 - 메서드, 속성은 변수처럼 생성)
    color = ""
    speed = 0
    name = ''
    count = 0
    
    def up_speed(self, value):   #클래스 사용 순서
        self.speed += value
    def down_speed(self, value):   #self는 이용시 필수
        self.speed -= value
    def __init__(self, value1, value2):  #field값 초기화  형식 암기!!!
        self.name = value1
        self.speed = value2
        car.count += 1
    def get_name(self):
        return self.name
    def get_speed(self):
        return self.speed
    def print_message() :
        print("시험 출력이다")  #field를 쓰지 않으면 self 생략 가능/ 인스턴스 즉 클래스의 인스턴스는 객체
        
mycar1 = car('red', 20)
print(mycar1.color, mycar1.get_speed(), mycar1.get_name(), car.count)
mycar2 = car('blue', 70)
print(mycar2.color, mycar2.get_speed(), mycar2.get_name(), car.count) #mycar2.count도 사용 가능
car.print_message()

#메서드 오브라이딩(재정의)
#통된 내용을 상위클래스에 두고 상속을 받음으로서 일관되고 효울적인 프로그래밍이 가능하다. 여기서 상위클래스 = 부모클래스, 상위클래스/ 하위클래스 = 서브클래스, 자식클래스
class Sedan(car) :
    def up_speed(self, value):
        self.speed += value
        if (self.speed >= 150) :
            self.speed = 150
class Trunk(car):
    pass


sedna1 = Sedan('red', 0)
truck1 = Trunk('blue', 0)

sedna1.up_speed(200)
truck1.up_speed(200)

print(sedna1.speed)
print(truck1.speed)





