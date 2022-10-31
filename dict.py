'''
filename = dict.py
딕셔너리(=객체) 사용법
'''
info = { }


#이름입력
info["name"] = input("이름입력:")

#나이 
info["age"] = input("나이입력:")

#주소 
info["add"] = input("주소입력:")

#주소삭제
# del info["add"]

#info 출력
for key in info:
    print(f"\n{key}\t{info[key]}")

# for 반복문과 딕셔너리 조합  for 키변수 in 딕셔너리 