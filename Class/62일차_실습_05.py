import sqlite3

try :
    conn = sqlite3.connect("data/sqlite2_db")
    
    cursor = conn.cursor()

    sql = '''create table if not exists item(
    code integer primary key,
    name text(30) unique not null,
    qty integer default 0,
    unit_price real default 0.0
    )'''
    cursor.execute(sql)  # sql 실행

    cursor.execute("insert into item values(1, '선풍기', 1, 150)")
    cursor.execute("insert into item values(2, '에어컨', 1, 200)")
    cursor.execute("insert into item values(3, '충전기', 1, 100)")
    cursor.execute("insert into item values(4, '키보드', 1, 70)")
    cursor.execute("insert into item values(5, '마우스', 1, 60)")
    conn.commit()  # db 반영

    sql = "select * from item"
    cursor.execute(sql)
    rows = cursor.fetchall()  # 레코드 가져오기

    for row in rows :
        print('조회 결과는 코드: ', row[0], '제품명: ',  row[1], '수량: ', row[2], '단가: ', row[3])

    print('검색된 레코드 수 : ', len(rows))
    
    code = input('코드 입력 : ')
    sql = f'select * from item where code like "%{code}%"'
    cursor.execute(sql)
    rows = cursor.fetchall()

    if rows :
        for row in rows :
            print(row)
    else :
        print('검색된 레코드 없음')

except Exception as e :
    print('db 연동 error : ', e)
    conn.rollback()

finally :
    cursor.close()
    conn.close()