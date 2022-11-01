'''
filename L finc2.py
지역변수, 전역변수 
'''
#함수선언
#1~10까지 합계
def mysum(n):
    total = 0
    for i in range(n+1):   #0~10 까지 반복  i(반복변수,i/j/k를 많이씀)
        total += i
    return total  #토탈값을 넘겨줄테니 받아라 


#함수실행(=호출)
num = int(input('입력'))
t1 = mysum(num)    
print('합계는', t1)

num = int(input('입력'))
t1 = mysum(num)
print('합계는', t1, '입니다')
