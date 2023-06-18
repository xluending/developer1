import os
import sys
import pymysql

config = {                  # MySQL데이터베이스를 사용하기 위해 환경변수를 딕셔너리로 생성함. 
    'host' : '127.0.0.1',   # MySql 이 동작하는 ipv4주소 
    'user' : 'developer1',  # MySql 설치할 때 정한 계정 
    'password' : '0000',    # MySql 설치할 때 정한 비밀번호
    'database' : 'test_db', # 생성한 데이터베이스
    'port' : 3306,          # MySql이 응용프로그램과 통신할 때 사용하는 포트번호 리터럴이 아닌 정수값으로 써야함
    'charset' : 'utf8',     # 한글을 사용하겠다는 설정 
    'use_unicode' : True    # 한글을 사용하겠다는 설정 
    }

def tableCreate() :
    try :
        print("----->")
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        sql = """create table  if not exists goods(
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


def item_create() :
    try : 
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        in_name = input("상품명을 입력하세요 : ")
    
        if in_name :
            sql = f"select * from goods where name = '{in_name}'"
            cursor.execute(sql)
            rows = cursor.fetchall()

            if len(rows) > 0 :
                print("이미 존재하고 있습니다. 추가로 등록할 상품을 입력하세요")
            else :
                print("<<<상품 등록입니다>>>")
                in_code = int(input("상품 코드를 입력하세요 : "))
                in_su = int(input("수량을 입력하세요 : "))
                in_dan = int(input("단가를 입력하세요 : "))

                sql = f"insert into goods(code, name, su, dan) values({in_code}, '{in_name}', {in_su}, {in_dan})"
                cursor.execute(sql)
                rows = cursor.fetchall()
                conn.commit()
                print("상품 등록을 성공했습니다.")
                print()
        else :
            print("상품 등록을 위해 상품명을 입력해주세요")
    
    except Exception as e :
        print("에러 발생 : ", e)
        conn.rollback()
    finally :
        cursor.close()
        conn.close()


def item_list() :
    try :
        conn = pymysql.connect(**config)
        cursor = conn.cursor()

        cursor.execute("select * from goods")
        rows = cursor.fetchall()
        print("<<<상품 목록 조회입니다>>>")
        print("===goods 테이블 조회1===")
        print("(code, name, su, dan)")
        for row in rows :
            print(row)
    except Exception as e :
        print("오류 : ", e)
        conn.rollback()
    finally :
        cursor.close()
        conn.close()

def search_code() :
    try : 
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        print("<<<상품 개별 조회(코드)입니다>>>")
        in_code = int(input("조회할 코드를 입력하세요 : "))
        sql = f"select * from goods where code = {in_code}"
        cursor.execute(sql)
        rows = cursor.fetchall()
        if len(rows) > 0 :
            print("===goods 테이블 조회2(코드)===")
            for row in rows :
                print("조회결과는 코드:{}, 상상품명:{}, 수량:{}, 단가:{} 입니다.".format(row[0], row[1], row[2], row[3]))
                print()

        else :
            print("조회결과 입력한 코드에 해당하는 상품이 없습니다.")

    except Exception as e :
        print("에러 : ", e)
        conn.rollback()
    finally :
        cursor.close()
        conn.close()


def search_name() :
    try : 
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        print("<<<상품 개별 조회(상품명)입니다>>>")
        in_name = input("조회할 상품을 입력하세요 : ")
        sql = f"select * from goods where name = '{in_name}'"
        cursor.execute(sql)
        rows = cursor.fetchall()
        if len(rows) > 0 :
            print("===goods 테이블 조회2(상품명)===")
            for row in rows :
                print("조회결과는 코드:{}, 상품명:{}, 수량:{}, 단가:{} 입니다.".format(row[0], row[1], row[2], row[3]))
                print()

        else :
            print("조회결과 입력한 코드에 해당하는 상품이 없습니다.")

    except Exception as e :
        print("에러 : ", e)
        conn.rollback()
    finally :
        cursor.close()
        conn.close()


if __name__ == "__main__" :  # 소스코드에서 제일 먼저 실행되는 시작점
    while True :
        os.system('cls')
        print("---상품관리---")
        print("상품    등록 : 1")
        print("상품목록조회 : 2")
        print("코드별  조회 : 3")
        print("상품명별조회 : 4")
        print("상품    수정 : 5")
        print("상품    삭제 : 6")
        print("상품관리종료 : 9")
    
        sel  = int(input("작업을 선택하세요 : "))
        if sel == 1 :
            item_create()
            os.system("pause")
        elif sel == 2 :
            item_list()
            os.system("pause")
        elif sel == 3 :
            search_code()
            os.system("pause")
        elif sel == 4 :
            search_name()
            os.system("pause")