'''
filename : list2.py
리스트 삭제, 조회
'''

members = [
    {'name': '김이름', 'age':20, 'addr' : '대구'},
    {'name': '이이름', 'age':30, 'addr' : '부산'},
    {'name': '최이름', 'age':40, 'addr' : '서울'}
]

##전체출력 이름과 주소 출력
name =input("검색할이름입력:")
for i in range(len(members)):  #검색할때도 사용가능. p.145
    if name in members[i]["name"]:     ##in을 사용했을때
    # if mem["name"].find(name) >= 0 :  ##.find를 사용했을때

        print(f'{members[i]["name"]} \t {members[i]["addr"]}')
    #삭제
        del members[i]    #i는 배열 인덱스를 가리킴.
        # i=i-1 
        break
    print(members)
