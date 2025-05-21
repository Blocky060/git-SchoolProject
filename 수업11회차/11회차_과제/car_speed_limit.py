class car :   
    color = ""
    speed = 0
    
    def up_speed(self, value):
        self.speed += value
        if (self.speed >= 150) :
            self.speed = 150
    def down_speed(self, value):   
        self.speed -= value
    def print_message() :
        print("시험 출력이다")  
        
mycar1 = car()
mycar2 = car()
mycar3 = car()

mycar1.color = '빨강'
mycar1.speed = 0

mycar2.color = '파랑'
mycar2.speed = 10

mycar3.color = '노랑'
mycar3.speed = 30

mycar1.up_speed(200)
mycar2.up_speed(50)
mycar3.up_speed(70)

print(mycar1.color, mycar1.speed)
print(mycar2.color, mycar2.speed)
print(mycar3.color, mycar3.speed)