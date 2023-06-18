# (1) 패키지
import pymysql
print(pymysql.version_info)

# (2) db 연동 환경변수
config = {                  # MySQL 데이터베이스를 사용하기 위해 환경변수를 딕셔너리로 생성함
    'host' : '127.0.0.1',   # MySQL 이 동작하는 ipv4 주소
    'user' : 'developer1',  # MySQL 설치할 떄 정한 계정
    'password' : '0000',    # MySQL 설치할 떄 정한 비밀번호
    'database' : 'work',    # MySQL 설치할 떄 생성한 데이터베이스
    'port' : 3306,          # MySQL 이 응용프로그램과 통신할 떄 사용하는 포트번호 (리터럴이 아닌 정수값으로 써야함)
    'charset' : 'utf8',     # 한글을 사용하겠다는 설정
    'use_unicode' : True }  # 한글을 사용하겠다는 설정

try :
    # (3) db 연동 객체
    conn = pymysql.connect(**config)
    # (4) sql 실행 객체
    cursor = conn.cursor()

    # (5) 테이블 조회
    sql = "show tables"
    cursor.execute(sql)
    tables = cursor.fetchall()

    # (6) 전체 table 목록 출력
    print(tables)

    # (7) table 유무
    if tables:
        print('table 있음')
    else:
        print('table 없음')

except Exception as e :
    print('db error  : ', e)

finally:
    cursor.close()
    conn.close()