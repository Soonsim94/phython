'''
filename : baseball.py
숫자야구게임
'''

# 컴퓨터 난수 3개
from random import randint
import sys

def cnt_strike(c1,c2,c3,n1,n2,n3):
    s = 0
    if c1 == n1:
        s += 1
    if c2 == n2:
        s += 1    
    if c3 == n3:
        s += 1
    return s

def cnt_ball(c1,c2,c3,n1,n2,n3):
    b=0
    if c1 == n2 or c1 == n3:
        b += 1
    if c2 == n1 or c2 == n3:
        b += 1
    if c3 == n1 or c3 == n1:
        b += 1  
    return b

def user_input() :
    n1,n2,n3 = input().split(' ')

    # 정수형 변환
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    return n1,n2,n3

while True:
    c1 = randint(1,9)
    while True:
        c2 = randint(1,9)
        if c1 != c2:
            break
    c3 = randint(1,9)
    print(c1,c2,c3)
    cnt = 0  #시도횟수
    s = 0
    
    # 맞거나 시도횟수
    while s < 3 and cnt < 3:   
        cnt +=1
        # 게이머가 숫자 3개 입력
        n1,n2,n3 = user_input()

        # 스트라익 수 계산
        s = cnt_strike(c1,c2,c3,n1,n2,n3)

        # 볼 수 계산
        b = cnt_ball(c1,c2,c3,n1,n2,n3) 

        print(f'스트라익:{s} ball:{b}')

    exitYn = input("게임을 계속할까요? Y,N")
    if exitYn in ['N','n']:
        break

