'''
filename : list2.py
리스트 삭제, 조회
'''

members = [
    {'name': '김이름', 'age':20, 'addr' : '대구'},
    {'name': '이이름', 'age':30, 'addr' : '부산'},
    {'name': '최이름', 'age':40, 'addr' : '서울'}
]

##전체출력
# for mem in members:
#     age = int(input("검색할나이입력:"))
#     if mem["age"] == age:
#         print(f'{mem["name"]}\t{mem["addr"]}')
#이름출력

##전체출력 이름과 주소 출력
name =input("검색할이름입력:")
for mem in members:  #검색할때도 사용가능. p.145
    if name in mem["name"]:     ##in을 사용했을때
    # if mem["name"].find(name) >= 0 :  ##.find를 사용했을때
        print(f'{mem["name"]}\t{mem["addr"]}')
