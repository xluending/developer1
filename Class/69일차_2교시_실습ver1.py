# 069일차-실습-0-1-해답-ver1
import os
import sys
import pymysql
config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'passwd' : 'root1234',
    'database' : 'test_db',
    'port' : 3306,
    'charset' : 'utf8',
    'use_unicode' : True 
    }
#--------------------------
#  069일차-실습-0-1-해답-ver1에서는 허수아비임 / 069일차-실습-0-1-해답-ver2의 217 line 에서 사용함  
'''
class InputFilter :
    def __init__(self):   
        self.inputValueFilter_result = False
        self.name = ''
        self.su = 0
        self.dan = 0
    def setName(self, name) :
        if name == '' or len(name) < 0 :
            print("공백일때 "+str(name)+" 의 정보는 부정확합니다.")
            self.inputValueFilter_result = False
        else:
            self.inputValueFilter_result = True
            self.name = name
        return self.inputValueFilter_result
        
    def setSu(self, su) :
        if su == 0 or su < 0 :
            print("0 이거나 음수일때 "+str(su)+" 의 정보는 부정확합니다.")
            self.inputValueFilter_result = False
        else:
            self.inputValueFilter_result = True
            self.su = su
        return self.inputValueFilter_result
    
    def setDan(self, dan) :
        if dan == 0 or dan < 0 :
            print("0나 음수일때 "+str(dan)+" 의 정보는 부정확합니다.")
            self.inputValueFilter_result = False
        else:
            self.inputValueFilter_result = True
            self.dan = dan
        return self.inputValueFilter_result
'''
#
#--------------------------
class GoodsFind :
    def __init__(self,find_sel,find_in_data=''):   
        #print('\n',sel)        
        self.read_sel = find_sel
        if find_sel == 3 or find_sel == 5 or find_sel == 6: 
            self.find_sql = "select * from goods where code =" + f"'{find_in_data}'"
        elif find_sel == 4 : 
            self.find_sql = "select * from goods where name =" + f"'{find_in_data}'"
        else :
            self.find_sql = "select * from goods"
    def goodsfind(self) :
        try :
            conn = pymysql.connect(**config) 
            cursor = conn.cursor()
            cursor.execute(self.find_sql)
            return cursor.fetchall()    # select 쿼리문의 실행 결과를 return함
                      # 쿼리의 실행결과가 없으면 요소의 갯수가 0인 리스트가 반환됨
        except Exception as e :
            print('db 연동 실패 : ', e)
            conn.rollback() # 실행 취소 
        finally:
            cursor.close()
            conn.close()
#--------------------------
def goodsDelete() :
    os.system('cls')
    print("<<<상품 목록 조회입니다>>>")
    gf1 = GoodsFind(2)
    rows = gf1.goodsfind()
    for row in rows :
        print("{} {} {} {} ".format(int(row[0]),row[1],int(row[2]),int(row[3])    ))
    try :
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        print("<<<삭제할 상품의 코드를 입력하세요>>>")
        in_code = int(input('삭제할 코드 입력 : '))
        sql = f"select * from goods where code = {in_code}"
        cursor.execute(sql) # sql문 실행 
        rows = cursor.fetchall()
        if rows :
            sql = f"delete from goods where code = {in_code}"
            cursor.execute(sql) # sql문 실행
            conn.commit() 
            print('삭제 성공했습니다.')
            os.system("pause")
        else :
            print('삭제 실패했습니다.')
            os.system("pause")
    except Exception as e :
        print('db 연동 실패 : ', e)
        conn.rollback() # 실행 취소 
    finally:
        cursor.close()
        conn.close()
    print("<<<상품 목록 조회입니다>>>")
    gf1 = GoodsFind(2)
    rows = gf1.goodsfind()
    for row in rows :
        print("{} {} {} {} ".format(int(row[0]),row[1],int(row[2]),int(row[3])    ))
#--------------------------
def goodsUpdate() :
    os.system('cls')
    print("<<<상품 수정입니다>>>")
    in_code = int(input('수정할 상품코드를 입력하세요 : '))
    up1 = GoodsFind(5,in_code)
    rows = up1.goodsfind()
    #
    try :
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        if rows : # select 쿼리 실행결과가 있는 경우
            print("<<<상품코드 조회결과입니다>>>")
            for row in rows :
                print("{} {} {} {} ".format(int(row[0]),row[1],int(row[2]),int(row[3])    ))
            yesNo = input('수정하시겠습니까>(y/n) : ')
            if yesNo == "y" or yesNo == "Y":
                print("<<<수정할 내용을 입력하세요.>>>")
                iValue = userInput()  
                sql = f"update goods set name = '{iValue[0]}' ,su = {iValue[1]} ,dan={iValue[2]} where code = {in_code}" 
                cursor.execute(sql) # sql문 실행
                conn.commit() 
                print("<<<수정을 완료했습니다>>>")
                print("<<<상품 수정 결과입니다>>>")
                print("{} {} {} {} ".format(int(in_code),iValue[0],int(iValue[1]),int(iValue[2])    ))
            else:
                print("<<<수정을 취소했습니다.>>>")
        else : # select 쿼리 실행결과가 없는 경우
            print('수정할 코드가 없습니다.')
            pass
    except Exception as e :
        print('db 연동 실패 : ', e)
        conn.rollback() # 실행 취소 
    finally:
        cursor.close()
        conn.close()
#--------------------------
class GoodsRead :
    def __init__(self,read_sel): # 생성자 : read_sel : 코드/상품명/all ,            
        self.read_sel = read_sel
        if read_sel == '코드' :  #  read_sql : "select * from goods where code =" / "select * from goods where name ="
            self.read_sql = "select * from goods where code ="
        elif read_sel == '상품명' : 
            self.read_sql = "select * from goods where name ="
        else :
            self.read_sql = "select * from goods"
    def goodsReadOne(self) :
        try :
            conn = pymysql.connect(**config)    
            cursor = conn.cursor() 
            #
            rows = []
            os.system('cls')

            if self.read_sel == '코드' :
                print("<<<상품 개별 조회({})입니다>>>".format(self.read_sel))
                in_code = int(input("조회할"+self.read_sel+"를 입력하세요 : "))
                sql = self.read_sql + f"'{in_code}'"
            elif self.read_sel == '상품명' : 
                print("<<<상품 개별 조회({})입니다>>>".format(self.read_sel))
                in_code = input("조회할"+self.read_sel+"를 입력하세요 : ")
                sql = self.read_sql + f"'{in_code}'"
            else :
                in_code = ''
                sql = self.read_sql
            cursor.execute(sql)
            rows = cursor.fetchall()
            if self.read_sel == '코드' or self.read_sel == '상품명' :
                if len(rows) > 0 :
                    print("===goods 테이블 조회2({})===".format(self.read_sel))
                    for row in rows :
                        print("조회결과 코드:{}, 품명:{}, 수량:{}, 단가:{} .".format(int(row[0]),row[1],int(row[2]),int(row[3])    ))
                else:
                    print("조회결과 입력한 {}에 맞는 상품이 없습니다".format(self.read_sel))
            else: # self.read_sel == 'all'일때
                if len(rows) > 0 :
                    print("<<<상품 목록 조회결과입니다>>>")
                    for row in rows :
                        print("{} {} {} {} ".format(int(row[0]),row[1],int(row[2]),int(row[3])    ))
                else:
                    print("조회결과 없습니다")           
        except Exception as e :
            print('db 연동 실패 : ', e)
            conn.rollback() # 실행 취소 
        finally:
            cursor.close()
            conn.close()
#--------------------------
def tableCreate() :
    try :
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        sql = """create table goods(
            code int primary key,
            name varchar(30) not null,
            su int default 0,
            dan int default 0
            )"""
        cursor.execute(sql)
        conn.commit()
    except Exception as e :
        print("오류 : ",e)
        conn.rollback()
    finally :
        conn.close()
        cursor.close()
#--------------------------
def userInput():
    while True :
        in_name = input("상품명을 입력하세요 : ") 
        alpha = in_name.isdigit()
        if alpha == True :
            print("상품명을 다시 입력해주세요.")
            continue
        break
    while True :
        in_su = int(input("수량을 입력하세요 : ")) 
        if in_su <= 0 :
            print("수량을 다시 입력해주세요.")
            continue
        break
    while True :
        in_dan = int(input("단가를 입력하세요 : "))
        if in_dan <= 0 :
            print("단가를 다시 입력해주세요.")
            continue
        break
    return in_name, in_su, in_dan
#--------------------------
def goodsCreate() :
    try :
        conn = pymysql.connect(**config)   
        cursor = conn.cursor()
        #
        os.system('cls')
        print("<<<상품 등록입니다>>>")
        in_code = int(input("등록할 상품코드를 입력하세요 : "))  #
        if in_code > 0 :
            c1 = GoodsFind(3,in_code)
            if len(c1.goodsfind()) :
                print("이미 존재하고 있습니다. 다른 코드를 입력하세요")
            else :
                iValue = userInput()
                #
                sql = f"insert into goods(code,name,su,dan) values({in_code},'{iValue[0]}', {iValue[1]},{iValue[2]})" 
                cursor.execute(sql)
                rows = cursor.fetchall()
                conn.commit()
                print("상품등록을 성공했습니다.")
                print()
        else :
            print("상품 등록을 위해 코드를 입력해 주세요")
    except Exception as e :
        print('오류 : ', e)
        conn.rollback() # 실행 취소 
    finally:
        cursor.close()
        conn.close()
#--------------------------
def goodsReadAll() :
    os.system('cls')
    print("<<<상품 목록 조회입니다>>>")
    gf1 = GoodsFind(2)
    rows = gf1.goodsfind()
    print("===goods 테이블 조회1===")
    print("(code, name, su, dan)")
    for row in rows :
        print(row)
#--------------------------
if __name__ == "__main__" :
    tableCreate()
    while True:
        os.system('cls')
        print("---상품관리---")
        print("상품    등록 : 1 ")
        print("상품목록조회 : 2 ")
        print("코드별  조회 : 3 ")
        print("상품명별조회 : 4 ")
        print("상품    수정 : 5 ")
        print("상품    삭제 : 6 ")
        print("상품관리종료 : 9 ")
        sel = int(input("작업을 선택하세요 : "))
        if sel == 1 :
            goodsCreate()
            os.system("pause")
        elif sel == 2 :
            goodsReadAll()
            os.system("pause")
        elif sel == 3 :
            r3 = GoodsRead('코드')
            r3.goodsReadOne()
            os.system("pause")
        elif sel == 4 :
            r4 = GoodsRead('상품명')
            r4.goodsReadOne()
            os.system("pause")
        elif sel == 5 :
            goodsUpdate()
            os.system("pause")
        elif sel == 6 :
            goodsDelete()
            os.system("pause")
        elif sel == 9 :
            print("상품관리를 종료합니다. ")
            os.system("pause")
            os.system('cls')
            sys.exit(0)
        else :
            print("잘못 선택했습니다. ")
            os.system("pause")