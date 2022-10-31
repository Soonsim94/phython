'''
filename : break.py
'''


users = [ { 'userno':100, 'username':'user1', 'salary':2000},   #객체값 
          { 'userno':101, 'username':'user2', 'salary':1000}, 
          { 'userno':102, 'username':'user3', 'salary':1500}
]

while True:
    print("1.추가 2. 삭제 3. 조회 4. 전체조회 5.종료")
    no = int(input("메뉴선택:"))
    if no == 1:
        print("추가")
        info={}   #변수선언 객체받을거다 
        info["userno"] =int(input("userno입력:")) 
        info["username"] =input("username입력:")
        info["salary"] =input("salary입력:")  #번호 int 사용!
        users.append(info)


#문자열과 리스트인 경우만 in을 씀. 
    elif no == 2:
        userno = int(input("삭제할 번호 입력:"))
        idx = 0;
        for obj in users:
            if obj["userno"] == userno:
                del users[idx]
                break   
            idx += 1


    elif no == 3:
        #번호를 입력(검색할번호입력)
        userno = int(input("조회할 번호 입력:"))
        for idx in users:
            if obj['userno'] == userno :
                print(f'{users[obj]["username"]} {users[obj]["salary"]}')
        #해당 번호의 이름과 급여 출력 

    elif no == 4:
        print("전체조회")
        for obj in users :
            print(f'{obj['userno']} \t {obj['salary']}')

        #for문(전체출력)
    elif no == 5:
        break
print("the end")



# name =input("검색할이름입력:")
# for i in range(len(members)):  
#     if name in members[i]["name"]:     

#         print(f'{members[i]["name"]} \t {members[i]["addr"]}')
   
#         del members[i]    
    
#         break
#     print(members)
