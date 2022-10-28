#입력 
s = input()   #90 80 30

#문자 자르기
kor,eng,mat = s.split(" ")

#정수형 변환
kor = int(kor)
eng = int(eng)
mat = int(mat)

#합계
total = kor + eng + mat
#출력 

#국어:00 영어:00 수학:00 합계는 00입니다. 
print("국어:{:5d} 영어:{} 수학:{} \n합계는 {} 입니다.".format(kor,eng,mat,total))
print(f"국어:{kor} 영어:{eng} 수학:{mat} 합계는 {total} 입니다.")

