import sqlite3

try :
    # db 연동 객체
    conn = sqlite3.connect("data/sqlite06_db")

    # sql 실행 객체
    cursor = conn.cursor()

    # table 생성
    sql = '''create table if not exists item(
    code integer primary key,
    name text(30) unique not null,
    qty integer default 0,
    price real default 0.0
    )'''
    cursor.execute(sql) # sql 실행
    

    # 상품 등록(레코드 추가)
    code = int(input('code 입력 : '))
    name = input('name 입력 : ')
    qty = int(input('qty 입력 : '))
    price = int(input('price 입력 : '))
    sql = f"insert into item values({code}, '{name}', {qty}, {price})"
    cursor.execute(sql)
    conn.commit()


    sql = "select * from item"
    cursor.execute(sql) 
    rows = cursor.fetchall() # 레코드 가져오기

    for row in rows:
        상품등록 = print('===상품등록=== \n상품코드 입력:', row[0], '\n상품명 입력:',  row[1], '\n수량 입력:', row[2], '\n단가 입력:', row[3],'\n상품등록을 성공했습니다.')

    print('누적된 레코드 수 : ', len(rows))
    

     # 레코드 조회(상품조회1)
    sql = "select * from item"
    cursor.execute(sql)
    rows = cursor.fetchall() # 레코드 가져오기

    print("===상품조회1===\n(code, name, qty, price)")
    for row in rows :
        print(row[0], row[1], row[2], row[3])

    print('검색된 레코드 수 : ', len(rows))
    

    # 상품 코드로 조회(상품조회2)
    code = input("조회할 코드를 입력하세요 : ")
    sql = f"select * from item where code like '%{code}%'"
    cursor.execute(sql) # 조회
    rows = cursor.fetchall() # 레코드 가져오기

    if rows :
        for row in rows :
            print('===상품조회2===\n조회할 코드를 입력하세요: {}\n조회결과는 코드: {}, 제품명: {}, 수량: {}, 단가: {} 입니다.'.format(row[0], row[0], row[1], row[2], int(row[3])))
    else :
        print('===상품조회2===\n조회할 코드를 입력하세요: {}\n조회 결과 입력한 코드에 맞는 상품이 없습니다.'.format(code))
        

except Exception as e :
    print('db 연동 error : ', e)
    conn.rollback()

finally :
    cursor.close()
    conn.close()