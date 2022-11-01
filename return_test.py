'''
filename : return_test.py
'''

def return_test():
    num = int(input())
    print("a 위치")
    if(num<10):
        return #경우의 수에 따라 리턴하도록 중간에 줄 수 있음. 
    print("b 위치")
    #return 함수 마지막 리턴은 생략가능. 없더라도 젤 마지막줄에 리턴이 있는것과 같음. 


return_test()