'''
filename : 3일차/user_manage.py
'''

'''======================
메뉴선택
리터값: 입력된 메뉴번호
======================='''
def menu_select():
    print("1.추가 2.삭제 3.조회 4.전체조회  5.전체삭제  6.종료  7.파일읽기  8.파일저장")
    no = int(input("메뉴선택:"))
    return no

'''======================
회원등록
매개변수 : 회원정보 딕셔너리{userno:100, username:'choi', salary:1000}
리터값: 없음
======================='''
def user_insert():
    info = { }
    info["userno"] = int(input("userno입력:"))
    info["username"] = input("username입력:")
    info["salary"] = int(input("salary입력:"))
    return info  

'''======================
회원삭제
매개변수 : 삭제할 회원번호
리터값: 없음
======================='''
def user_delete(userno):
    idx = 0;
    for obj in users:
        if obj["userno"] == userno:
            del users[idx]
            break 
        idx += 1

'''======================
회원조회
매개변수 : 조회할 회원번호
======================='''
def user_select(userno):
    #해당 번호의 이름과 급여 출력
    for obj in users:
        if obj['userno'] == userno :
            print(f'{obj["userno"]} \t {obj["salary"]}' )

'''======================
회원전체조회
======================='''
def user_selectall():
    print("전체조회")    
    for obj in users:
        print(f'{obj["userno"]} \t {obj["salary"]}' )  


'''======================
회원전체삭제
======================='''
def user_deleteall():
    users.clear()

users = [ ] 

while True:
    #메뉴선택
    no = menu_select()

    if no == 1:
        info = user_insert()
        users.append(info)
    elif no == 2:
        userno = input("삭제할 번호 입력:")
        user_delete(userno)
    elif no == 3:
        #번호를 입력
        userno = int(input("조회할 번호 입력:"))
        user_select(userno)
    elif no == 4:
        user_selectall() 
    elif no == 5:
        user_deleteall()    
    elif no == 6:
        break

print("the end")