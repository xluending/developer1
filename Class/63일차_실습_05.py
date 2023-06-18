import pymysql

config ={
    'host' : '127.0.0.1',
    'user' : 'developer1',
    'password' : '0000',
    'database' : 'test_db',
    'port' : 3306,
    'charset' : 'utf8',
    'use_unicode' : True}

try :
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    # (1) table 생성
    sql = '''create table if not exists tb1(
    name varchar(20),
    age int,
    num int
    )'''
    cursor.execute(sql)

    # (2) 레코드 추가
    name = input('이름 입력 : ')
    age = int(input('나이 입력 : '))
    num = int(input('수량 입력 : '))

    sql = f"insert into tb1 values('{name}', {age}, {num})"
    cursor.execute(sql)
    conn.commit()

    # 테이블 조회
    sql = 'select * from tb1'
    cursor.execute(sql)
    rows = cursor.fetchall()

    for row in rows :
        print('===상품등록===\n이름입력 : {}\n나이 입력 : {}\n수량입력 : {}\n회원등록을 성공했습니다.'.format(row[0], row[1], row[2]))

    # 상품 조회
    name = input('조회할 이름을 입력하세요 : ')
    sql = f"select * from tb1 where name like '%{name}%'"
    cursor.execute(sql)
    rows = cursor.fetchall()

    if rows :
        for r in rows :
            print('===상품조회===\n조회할 이름을 입력하세요 : '%{name}%'\n조회결과는 이2름 : {}, 나이 : {}, 수량 : {} 입니다.'.format(row[0], row[1], row[2]))
    else :
        print('===상품조회===\n조회할 이름을 입력하세요 : '%{name}%'\n조회결과는 이름에 맞는 회원이 없습니다.')

except Exception as e :
    print('db error : ', e)
    conn.rollback()

finally :
    cursor.close()
    conn.close()