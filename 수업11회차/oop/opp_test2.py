class car :   #현실세계의 사물을 컴퓨터 안에서 구현할려고 고안한 개념 (field) (자용차의 기능은 함수 - 메서드, 속성은 변수처럼 생성)
    color = ""
    speed = 0
    name = ''
    
    def up_speed(self, value):   #클래스 사용 순서
        self.speed += value
    def down_speed(self, value):   #self는 이용시 필수
        self.speed -= value
    def __init__(self, value1, value2):  #field값 초기화  형식 암기!!!
        self.name = value1
        self.speed = value2
    def get_name(self):
        return self.name
    def get_speed(self):
        return self.speed
    def print_message() :
        print("시험 출력이다")  #field를 쓰지 않으면 self 생략 가능/ 인스턴스 즉 클래스의 인스턴스는 객체
        
mycar1 = car('red', 20)
mycar2 = car('blue', 70)

print(mycar1.color, mycar1.get_speed(), mycar1.get_name())
print(mycar2.color, mycar2.get_speed(), mycar2.get_name())