'''
filename : lambda.py
매개변수 함수를 전달하고자 할때 함수선언을 람다식으로 표현
'''

# def print_hi():
#     print("hi")


def print_hello():
    print("안녕하세요")

def call_10(func):
    for i in range(10):
        func()

call_10(print_hello)
call_10(lambda : print("hi"))

