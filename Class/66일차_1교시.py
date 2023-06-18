class clac_class11 :
    # 멤버 변수
    num1 = num2 = 0

    # 생성자
    def __init__(self, x, y) :
        self.num1 = x
        self.num2 = y

    # 메서드
    def div(self):
        return self.num1 / self.num2
    def squ(self):
        return self.num1 ** self.num2
    
obj = clac_class11(int(input("정수를 입력하세요 : ")), int(input("정수를 입력하세요 : ")))
print("나눗셈", obj.div())
print("제곱", obj.squ()) 