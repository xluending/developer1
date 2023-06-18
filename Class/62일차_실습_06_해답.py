# 062일차-실습-0-6-해답
import os
import sys
import sqlite3
try :
    # (1) db 연동 객체 
    conn = sqlite3.connect("data/sqlite2_db") # db 생성 -> 연결 object
    # sql 실행 객체 
    cursor = conn.cursor()

    # (2) item table 생성
    sql= """create table if not exists item(
        code integer primary key,
        name text(30) unique not null,
        qty integer default 0,
        unit_price real default 0.0)
        """
    cursor.execute(sql)
    conn.commit() # db 반영
    while True :
        # 상품등록 
        in_code = int(input('상품코드 입력 : '))
        sql = f"select * from item where code = {in_code}"
        cursor.execute(sql)
        rows = cursor.fetchall()

        if len(rows) > 0:
            print('존재하는 코드입니다.')
            os.system("pause")
            os.system('cls')
            continue
        else :
            in_name = input('상품명 입력 : ')
            in_qty = int(input("수량 입력 : "))
            in_unit_price = int(input("단가 입력 : "))
            sql = f"insert into item(code,name,qty,unit_price) values({in_code},'{in_name}',{in_qty},{in_unit_price})"
            cursor.execute(sql)
            conn.commit()
            print('상품 등록을 성공했습니다.')
            break

    # (4) 모든 레코드 조회
    cursor.execute("select * from item")
    rows = cursor.fetchall()
    print("===상품조회1===")
    print("(code, name, qty, price)")
    for row in rows :
        print(row)

    # (5) 단일 레코드 조회  
    in_code = int(input("조회할 코드를 입력하세요 : "))
    sql = f"select * from item where code = {in_code}"
    cursor.execute(sql)
    rows = cursor.fetchall()
    if rows :
        for row in rows :
            print("조회결과는 코드:{}, 제품명:{}, 수량:{}, 단가:{} 입니다.".format(row[0],row[1],row[2],int(row[3])))
    else:
        print("조회결과는 코드:{}는 없습니다.".format(in_code))
except Exception as e :
    print('db 연동 실패 : ', e)
    conn.rollback() # 실행 취소 
finally:
    cursor.close()
    conn.close()