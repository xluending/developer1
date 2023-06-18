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

try :
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    # (1) table 생성
    
    sql = """create table if not exists goods(
    code int primary key,
    name varchar(30) not null,
    su int default 0,
    dan int default 0
    )"""
    cursor.execute(sql)
    

    # (2) 레코드 추가
    '''
    code = int(input('코드 입력 : '))
    name = input('상품명 입력 : ')
    su = int(input('수량 입력 : '))
    dan = int(input('단가 입력 : '))

    sql = "insert into goods values({code}, '{name}', {su}, {dan})"
    cursor.execute(sql)
    conn.commit() # db 반영
    '''

    # (5) 레코드 수정
    # code 이용 -> 상품명, 수량, 단가 수정
    '''
    code = int(input('수정할 코드 입력 : '))
    name = input('수정할 상품명 입력 : ')
    su = int(input('수정할 수량 입력 : ' ))
    dan = int(input('수정할 단가 입력 : '))

    sql = f"update goods set name='{name}', su={su}, dan={dan}, where code={code}"
    cursor.execute(sql)
    conn.commit()
    '''

    # (6) 레코드 삭제
    code = int(input('삭제할 코드 입력 : '))
    sql = f"select * from goods where code = {code}"
    cursor.execute(sql) # sql문 실행
    rows = cursor.fetchall()

    if rows :
        # 레코드 1개 출력 : index 이용
        print('레코드 삭제')
        
        '''sql = f"delete from goods where code = {code}"
        cursor.execute(sql) # sql문 실행
        conn.commit()'''
        
    else :
        print('해당 code 없음')

    # (3) 전체 목록 보기
    sql = "select * from goods"
    cursor.execute(sql) # sql문 실행
    rows = cursor.fetchall() # 전체 검색
    # print(type(dataset)) # <class 'tuple'>

    # 레코드 출력 : 양식문자
    for r in rows : # fecthone()
        # print(r) # tuple type 출력
        print('%d %s %d %d'%r)

    print('검색된 레코드 수 : ', len(rows))

    # (4) 상품명 조회
    name = input('\n조회할 상품명 입력 : ')
    sql = f"select * from goods where name like '%{name}%'"
    cursor.execute(sql) # sql문 실행
    rows = cursor.fetchall()

    if rows :
        # 레코드 1개 출력 : index 이용
        for r in rows :
            print(r[0], r[1], r[2], r[3])
        else :
            print('해당 상품 없음')


except Exception as e:
    print('db 연동 오류 : ', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()