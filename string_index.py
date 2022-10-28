'''
filename : string_index.py
문자열 인덱싱(자르기)
'''

#인덱싱
a = "901210"

#한글자만 추출
print("첫번째문자",a[0])   #첫번째부터
print("마지막문자",a[-1])    #뒤에서부터 
print("출생년도",a[:2])   #인덱스는 범위주기 안됨. 
print("출생월",a[ : ])   
print("indexerror",a[7:])