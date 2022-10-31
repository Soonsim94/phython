'''
dict 4명 
'''


list = []

for i in range(3):
    info = { }

    info["name"] = input("이름입력:")

    info["age"] = input("나이입력:")

    info["add"] = input("주소입력:")
    
    #리스트에 추가
    list.append(info)

print(list)

    #리스트출력
for mem in list:  # for 변수 in 배열 : 
        print(f'{mem["name"]} \t {mem["age"]}')  #print(변수["출력명"])

    