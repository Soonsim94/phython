'''
filename : baseball.py
숫자야구게임 
'''

# 컴퓨터 난수 3개
from random import randint
import sys

c1 = randint(1,9)
c2 = randint(1,9)
c3 = randint(1,9)

cnt = 0 #시도횟수

s = 0
while s < 3 and cnt < 5:  
    cnt +=1
    # 게이머가 숫자 3개 입력
    n1,n2,n3 = input().split(' ') 

    # 정수형 변환
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)

    #스트라이크, 볼 초기화 
    s = 0 
    b = 0 

    # 스트라익 수 계산 

    if c1 == n1:
        s += 1

    if c2 == n2:
        s += 1 

    if c3 == n3:
        s += 1

    # 볼 수 계산 
    if c1 == n2 or c1 == n3:
        b += 1 

    if c2 == n1 or c2 == n3:
        b += 1 

    if c3 == n1 or c3 == n2:
        b += 1 

    print(f'스트라이크:{s} ball:{b}')

#스트라익 3이면 "축하"
    #시도횟수 3번만에 "천재"
    #시도횟수 4번만에 "우수"
    #아니면 "천재"
#스트라익이 3이 아니면 "게임오버"

if s == 3:
    print("축하")
    if cnt == 3:
        print("천재")
    elif cnt == 4:
        print("우수")
    else :
        print("보통")
else :
    print("게임오버")              

print("게임종료")
    
