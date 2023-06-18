class Employee :
    name = None
    pay = 0

    def __init__(self, name):
        self.name = name
    
    def pay_calc(self):
        pass

class Permanent(Employee):
    def __init__(self, name) :
        super() .__init__(name)

    def pay_calc(self, base, bouns):
        self.pay = base + bouns
        print('총 수령액 : ', format(self.pay, '3,d'), '원')

class Temporary(Employee):
    def __init__(self, name):
        super() .__init__(name)

    def pay_calc(self, tpay, time):
        self.pay = tpay * time
        print('총 수령액 : ', format(self.pay, '3,d'), '원')

class Alba(Employee):
    def __init__(self, name):
        super() .__init__(name)
    
    def pay_calc(self, money, wtime):
        if wtime >= 160 :
            self.pay = money * wtime + (money*8)
        elif wtime < 160 :
            self.pay = money * wtime
        print('총 수령액 : ', format(self.pay, '3,d'), '원')
    
p = Permanent("이순신")
p.pay_calc(3000000, 200000)

t = Temporary("홍길동")
t.pay_calc(15000, 80)

w = Alba("김종현")
w.pay_calc(20000, 160)