class Rectangle :
    width = height = 0

    def calc(self, width, height):
        self.width = width
        self.height = height

    def area_calc(self):
        return self.width * self.height
    
        
    def circum_calc(self):
        return (self.width + self.height) * 2


Ans = Rectangle()
Ans.calc(10, 5)
print("사각형의 넓이 : ", Ans.area_calc())
print("사각형의 둘레 : ", Ans.circum_calc())