class car :   #현실세계의 사물을 컴퓨터 안에서 구현할려고 고안한 개념 (field) (자용차의 기능은 함수 - 메서드, 속성은 변수처럼 생성)
    color = ""
    speed = 0
    
    def up_speed(self, value):   #클래스 사용 순서
        self.speed += value
    def down_speed(self, value):   #self는 이용시 필수
        self.speed -= value
    def print_message() :
        print("시험 출력이다")  #field를 쓰지 않으면 self 생략 가능/ 인스턴스 즉 클래스의 인스턴스는 객체
        
mycar1 = car()
mycar2 = car()
mycar3 = car()

mycar1.color = '빨강'
mycar1.speed = 0

mycar2.color = '파랑'
mycar2.speed = 10

mycar3.color = '노랑'
mycar3.speed = 30

mycar1.up_speed(30)
mycar2.up_speed(50)
mycar3.up_speed(70)

print(mycar1.color, mycar1.speed)
print(mycar2.color, mycar2.speed)
print(mycar3.color, mycar3.speed)