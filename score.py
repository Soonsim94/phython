'''
점수 3개를 입력받아서 
합계를 구하는 프로그램. 
수도코드 
'''
#입력 
s = input()   #90 80 30


#문자 자르기
kor,eng,mat = s.strip().split(" ") #앞뒤에 여백이 있을때 나는 오류 방지 

#정수형 변환
kor = int(kor)
eng = int(eng)
mat = int(mat)

#합계
total = kor + eng + mat

#평균

p = total / 3

if p >= 90:
    print("수")
elif p >= 80:
    print("우")
elif p >= 70:
    print("미")
else : 
    print("양")


# #출력  평균이 90이상 수 / 80이상 우 70 미 양 
# print(f"90:{수} 영어:{eng} 수학:{mat} 합계는 {total} 입니다.")