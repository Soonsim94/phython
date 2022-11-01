'''
filename : func1.py
매개변수와 리턴이 없는 함수
'''
#함수선언  #선언하고 넘어감 (실행내용x)
def print_3_hello(greeting, n=2):  #매개변수 
    for i in range(n): #함수가 실행후 끝날때까지만 존재 (i)
        print(greeting, end=" ")   #에러:argument (함수나 인수 잘못주었을때/갯수,타입오류)
                        # 옆으로 출력하게 해줌.

#함수호출 
g = "안녕하세요"
n=10
print_3_hello(g,n)
print( )
print_3_hello(n=3, greeting="hi")  #키워드 매개변수. 직접 지정 가능. (파이썬만가능)

print('a','b','c',sep='-')  #sep : 값을 여러개 출력할때 , 로 이어서 출력.
input()
