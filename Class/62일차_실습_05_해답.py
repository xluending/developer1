#062일차-실습-0-5-해답
import sqlite3
#print(sqlite3.sqlite_version_info) 
try :
    # (1) db 연동 객체
    conn = sqlite3.connect("data/sqlite2Q_db") # db 생성 -> 연결 object
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
 
    # (3) item table 에 로우(레코드) 삽입 : C
    # 이하 로직은 삽입 하기 이전에 테이블에 로우가 이미 존재하는지 검사하여
    # 있는 경우에는 삭제작업(delete 문)을 수행한 후,  삽입작업(insert 문)을 하고,
    # 없는 경우에만 삭제작업(delete 문)을 생략하고 삽입작업(insert 문)을 하도록 설계하였다.
    sql = "select * from item"
    cursor.execute(sql) # 조회
    dataset = cursor.fetchall()
    # (디버깅용 코드)
    #print("==")
    #print(type(dataset))
    #print(len(dataset))
    #print(dataset)
    #print(dataset[len(dataset)-1])
    #print(  type(dataset[len(dataset)-1])  )
    #print("==")
    #
    if len(dataset) > 0 : # null 이 아닌경우임 : 검색결과가 존재하는 경우임
        # 레코드 추가하기 이전에 item테이블 로우 모두 삭제
        cursor.execute("delete from item")
        conn.commit() # db 반영
    else :       # null 인 경우임 : 검색결과 아무것도 없는 경우임
        pass
    #
    # 레코드 삽입
    cursor.execute("insert into item values(1,'선풍기',1,150)")
    cursor.execute("insert into item values(2,'에어콘',1,200)")
    cursor.execute("insert into item values(3,'충전기',1,100)")
    cursor.execute("insert into item values(4,'키보드',1,70)")
    cursor.execute("insert into item values(5,'마우스',1,60)")
    conn.commit() # db 반영
 
    # (4) 모든 레코드 조회
    cursor.execute("select * from item")
    rows = cursor.fetchall()
    print("(code, name, qty, price)")
    for row in rows :
        print(row)
 
    # (5) 단일 레코드 조회  
    in_code = int(input("조회할 코드를 입력하세요 : "))
    sql = f"select * from item where code = {in_code}"
    cursor.execute(sql)
    rows = cursor.fetchall()
 
    for row in rows :
        print("조회결과는 코드:{}, 제품명:{}, 수량:{}, 단가:{} 입니다.".format(row[0],row[1],row[2],int(row[3])))
 
except Exception as e :
    print('db 연동 실패 : ', e)
    conn.rollback() # 실행 취소
finally:
    # object.close()
    cursor.close()
    conn.close()