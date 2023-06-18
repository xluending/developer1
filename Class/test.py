base = 3000000

bonus = 200000

pay = base + bonus  # 급여 = 기본급+상여금

print('총 수령액1 : ', format(pay, '3,d'),'원')  # 

print('총 수령액2 : ', format(pay, '1,d'),'원')

print('총 수령액2 : ', format(pay, '9,d'),'원')  # 9 = 출력해야되는 자리 수
print('총 수령액2 : ', format(pay, '15,d'),'원')



class Rectangle :
    width = height = 0


    def area_calc(self, width, height):
        self.squ_area = width * height
        print(int(input("가로 입력 : ", "세로 입력 : ")))

    def circum_calc(self, width, height):
        self.squ_circum = (width + height) * 2
        print(int(input("가로 입력 : ", "세로 입력 : ")))


Ans = Rectangle
Ans.area_calc()