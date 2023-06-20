#071일차-실습-0-5-해답.
# ndarray의 메서드 확인 
import numpy as np
num1 =0
for i in dir(np.ndarray) :
    if not i.startswith("_") :
        if type(np.ndarray.__dict__[i]) == type(np.ndarray.var)  :
            #print(i)
            num1 +=1
print('ndarray 메서드의 갯수',num1)
 
# 리스트 클래스의 메서드 확인 
num1=0
for i in dir('list') :
    if not i.startswith("_") :
        #print(i)
        num1 +=1
print('리스트 메서드의 갯수',num1)
 
import numpy as np
# ndarray의 속성(변수) 확인 
num1 =0
for i in dir(np.ndarray) :
    if not i.startswith("_") :
        if type(np.ndarray.__dict__[i]) != type(np.ndarray.var)  :
            #print(i)
            num1 +=1
print('ndarray 속성의 갯수',num1)
 
# 리스트 클래스의 메서드 확인 
num1=0
for i in dir('list') :
    if not i.startswith("_") :
        #print(i)
        num1 +=1
print('리스트 메서드의 갯수',num1)
