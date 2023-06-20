# 실습-0-4-해답
import numpy as np
import pandas as pd 
#
jumsu = {'홍길동' : [50,60,50],'이순동' : [60,60,60],'강감동' : [100,90,90],'유관동' : [80,80,90],
'홍길도' : [50,45,50],'이순도' : [80,70,66],'강감도' : [64,49,50],'유관도' : [60,50,50],'홍길재' : [50,45,51],
'이순재' : [80,70,61],'강감재' : [64,49,51],'유관재' : [60,50,51],'강환석' : [95,95,95]}
# 딕셔너리의 요소중에 평균 점수가 60점 미만인 것만 필터링 하는 루틴
jumsu2 = dict(  {   key : round(np.mean(value),2)   for key, value  in jumsu.items() if np.mean(value)<60  } )
                                                                     # jumsu 딕셔너리의 밸류 중에서 평균이 60 미만인 것만 
                                                                     # 뽑아낸 쌍을 items() 튜플에 할당하고 튜플의 요소를 
                                                                     # unpacking하여 key, value 라는 변수에 할당하는 for문 
                                                                     # items() 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items  
                                                                     # 객체로반환함. 이 구절에서는 튜플로 묶은 dict_items 객체를 
                                                                     # in 연산자 왼쪽의  key, value에 unpacking하였다
                           # for 문으로 발생한 key, value를 
                           # 각각 key와 round(np.mean(value),2)의 쌍으로 구성하고 이것을
                # dict() 형변환 함수로 변환하여 jumsu2 딕셔너리로 생성한다.
#
#print(type(jumsu2)) # 서비스 코드임
#print(jumsu2)       # 서비스 코드임
#
jumsu3 = pd.Series(jumsu2)
for i in jumsu3.index:
    print(i, end="-")
print()
for i in jumsu3:
    print(i, end="--")
print()