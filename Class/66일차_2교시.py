class clac_class12 :
    num1 = num2 = 0

    def member_clear(self, x, y) :
        self.num1 = x
        self.num2 = y

    def div(self) :
        return self.num1 / self.num2
    
    def squ(self) :
        return self.num1 ** self.num2
    
obj = clac_class12()
obj.member_clear(4, 2)
print('나누기 = ', obj.div())
print('제곱 = ', obj.squ()) 