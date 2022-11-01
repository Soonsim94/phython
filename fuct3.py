'''
filename : func3.py
전역변수
'''

total = 0

def mysum():
    global total    #전역변수 토탈 쓰겠다 선언. 
    for i in range(11):
        total += i

mysum()
print(total)  #함수 안과 밖의 토탈은 다르다.

