# 클래스 정의
class calc_class :
    # 변수 선언
    x = y = 10
    # 생성자 : 객체 생성 + [멤버변수 초기화] 
    def __init__(self, a, b):
        print('~~객체 생성~~')
        self.x = a # 10
        self.y = b # 20
    # 멤버 함수(기능)
    def plus(self): # self : 멤버(변수+함수) 참조 객체 
        p = self.x + self.y
        '''
        p : 지역변수 
        self.x, self.y : 전역변수  
        '''
        return p 
    def minus(self):
        m = self.x - self.y
        return m
# class(1) -> object(n) 생성 
#

obj1 = calc_class(10, 20) # 생성자 -> 객체1  
# object.member()  
print('plus = ', obj1.plus()) # plus =  30
print('minus =', obj1.minus()) # minus = -10