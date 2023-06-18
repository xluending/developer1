import os
import sys
import pymysql
config = {
    'host' : '127.0.0.1',
    'user' : 'developer1',
    'passwd' : '0000',
    'database' : 'studid',
    'port' : 3306,
    'charset' : 'utf8',
    'use_unicode' : True 
    }


def createID():
    try :
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        os.system('cls')

        print('<<< 등록 >>>')
        in_studID = int(input("등록하실 학번을 입력하세요 : "))
        if in_studID > 0 :
            sql = f"select * from stud where studid = {in_studID}"
            cursor.execute(sql)
            rows = cursor.fetchall()
            if len(rows) > 0 :
                print('등록된 학번이 존재합니다.')
            else :
                in_name = input("이름을 입력하세요 : ")
                in_jumin1 = int(input("주민번호 앞 6자리 입력 : "))
                in_jumin2 = int(input("주민번호 뒤 7자리 입력 : "))
                sql = f"insert into stud(studID, name, jumin1, jumin2) values({in_studID}, '{in_name}', {in_jumin1}, {in_jumin2})"
                cursor.execute(sql)
                rows = cursor.fetchall()
                conn.commit()
                print("등록을 성공했습니다.")
                print()
        else :
            print('8자리 내 숫자로 학번을 입력해주세요.')
    except Exception as e:
        print('오류 : ', e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def searchID() :
    try :
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        os.system('cls')

        print("<<< 학번으로 조회할 수 있습니다 >>>")
        in_studID = input("조회할 학번을 입력해주세요 : ")
        sql = f"select * from stud where studID = {in_studID}"
        cursor.execute(sql)
        rows = cursor.fetchall()
        if len(rows) > 0 :
            print("=== 학번 조회 결과 ===")
            for row in rows :
                print("학번: {}, 이름: {}, 주민등록번호: {}-{}".format(int(row[0]), row[1], int(row[2], int(row[3]))))
        else :
            print("조회 가능한 학번이 없습니다.")
    except Exception as e:
        print("오류 : ", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def editID() :
    try :
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        print("<<< 수정할 학번을 입력해주세요 >>>")
        in_studID = int(input("학번 입력 : "))
        sql = f"select * from stud where studID = {in_studID}"
        cursor.execute(sql)
        rows = cursor.fetchall()
        if rows :
            for row in rows :
                print("학번: {}, 이름: {}, 주민등록번호: {}-{}".format(int(row[0]), row[1], int(row[2], int(row[3]))))
        
        choose = input("수정하시겠습니다?(Y/N) : ")
        if choose == 'y' :
            print("<<< 수정하기 >>>")
            in_name = input("이름 : ")
            in_jumin1 = int(input("주민등록 앞 6자리"))
            in_jumin2 = int(input("주민등록 뒤 7자리"))
            sql = f"update stud set name='{in_name}', jumin1={in_jumin1}, jumin2={in_jumin2} where studID={in_studID}"
            cursor.execute(sql)
            conn.commit()
            print("수정을 완료했습니다.")
            print('<<< 수정 결과 >>>')
            sql = f"select * from stud where sutdID = {in_studID}"
            cursor.execute(sql)
            rows = cursor.fecthall()
            if rows :
                for row in rows:
                    print("학번: {}, 이름: {}, 주민등록번호: {}-{}".format(int(row[0]), row[1], int(row[2], int(row[3]))))
        elif choose != 'y' :
            pass
    except Exception as e :
        print('오류 : ', e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def deleteID() :
    try :
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        print("<<< 삭제할 학번을 입력해주세요 >>>")
        in_studID = int(input("삭제할 학번 입력 : "))
        sql = f"select * from stud where studID = {in_studID}"
        cursor.execute(sql)
        rows = cursor.fetchall()
        if rows :
            sql = f"delete from stud where studID = {in_studID}"
            cursor.execute(sql) # sql문 실행
            conn.commit()
            print('삭제 성공했습니다.')
            os.system("pause")
        else :
            print('삭제 실패했습니다.')
            os.system("pause")
    except Exception as e :
        print('오류 : ', e)            
        conn.rollback() # 실행 취소 
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__" :
    while True:
        os.system('cls')
        print("---상품관리---")
        print("학번 등록 : 1 ")
        print("학번 조회 : 2 ")
        print("학번 수정 : 3 ")
        print("학번 삭제 : 4 ")
        sel = int(input("작업을 선택하세요 : "))
        if sel == 1 :
            createID()
            os.system("pause")
        elif sel == 2 :
            searchID()
            os.system("pause")
        elif sel == 3 :
            editID()
            os.system("pause")
        elif sel == 4 :
            deleteID()
            os.system("pause")
        else :
            print("잘못 선택했습니다.")
            os.system("pause")