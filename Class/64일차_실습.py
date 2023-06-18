import os
import sys
import pymysql

config = {                  # MySQL데이터베이스를 사용하기 위해 환경변수를 딕셔너리로 생성함. 
    'host' : '127.0.0.1',   # MySql 이 동작하는 ipv4주소 
    'user' : 'developer1',        # MySql 설치할 때 정한 계정 
    'password' : '0000',  # MySql 설치할 때 정한 비밀번호
    'database' : 'test_db', # 생성한 데이터베이스
    'port' : 3306,          # MySql이 응용프로그램과 통신할 때 사용하는 포트번호 리터럴이 아닌 정수값으로 써야함
    'charset' : 'utf8',     # 한글을 사용하겠다는 설정 
    'use_unicode' : True    # 한글을 사용하겠다는 설정 
    }

def add_item() :
    try :
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        in_code = input("추가할 코드를 입력하세요 : ")

        if in_code :
            sql = f"select * from tb64 where code ='{in_code}'"
            cursor.execute(sql)
            rows = cursor.fetchall()

            if len(rows) > 0 :
                print("이미 존재하고 있습니다. 다른 코드를 입력하세요")
            else :
                in_name = input("상품명을 입력하세요 : ")
                in_su = int(input("수량을 입력하세요 : "))
                in_dan = int(input("단가를 입력하세요 : "))
                sql = f"insert into tb64(code, name, su, dan) values({in_code}, '{in_name}', {in_su}, {in_dan})"
                cursor.execute(sql)
                rows = cursor.fetchall()
                conn.commit()
                print("등록을 성공했습니다.")
                print()
        else :
            print("등록을 위한 코드를 입력해주세요.")

    except Exception as e :
        print("db error : ", e)
        conn.rollback()
    finally :
        cursor.close()
        conn.close()

def search_all() :
    try :
        conn = pymysql.connect(**config)
        cursor = conn.cursor()

        cursor.execute("select * from tb64")
        rows = cursor.fetchall()
        print("===모든 상품 조회===")
        print("(code, name, su, dan)")
        print("검색된 레코드 수 : ", len(rows))

        for row in rows :
            print(row)
    
    except Exception as e :
        print("db error : ", e)
        conn.rollback()
    finally :
        cursor.close()
        conn.close()

def search() : 
    try :
        conn = pymysql.connect(**config)
        cursor = conn.cursor()

        search_name = input("조회할 상품을 입력하세요 : ")
        sql = f"search * from tb64 where NAME = '{search_name}'"
        cursor.execute(sql)
        rows = cursor.fetchall()

        if len(rows) > 0 :
            print("===상품 조회===")
            for row in rows :
                print("조회 결과는 코드:{}, 상품:{}, 수량:{}, 단가:{} 입니다.".format(row[0], row[1], row[2], row[3]))
            else :
                print("조회결과 입력한 상품이 없습니다.")

    except Exception as e :
        print('db error : ', e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
            
if __name__ == "__main__" :  # 소스코드에서 제일 먼저 실행되는 시작점
    while True :
        os.system('cls')
        print("---상품관리---")
        print("상품 등록 : 1")
        print("상품 전체 목록 조회 : 2")
        print("상품 개별 조회 : 3")
        
        sel  = int(input("작업을 선택하세요 : "))
        if sel == 1 :
            add_item()
            os.system("pause")
        elif sel == 2 :
            search_all()
            os.system("pause")
        elif sel == 3 :
            search()
            os.system("pause")