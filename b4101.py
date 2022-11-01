'''
filename : b4101.py
'''
'''
    매개변수: 숫자 2개
    리턴값 : Yes, No, 0 
'''

#반복문
    #두 수를 입력
#####함수를 호출    
def compare (a,b):
    result = 0
    #두 수가 0이면 종료
    if a==0 and b==0:
        result = 0
    #크면   Yes
    if a > b :
        result = "Yes"
     #아니면 No
    else :
        result = "No"
    return result


#함수 

    #두 수를 입력
while True:

    a,b = input().split(" ");
    a = int(a)
    b = int(b)
    result = compare (a,b)
    #두 수가 0이면 종료 
    result = compare(a,b)
    if result = 0:
        break
    else :
        print ("No")
    
    #크면   Yes, #아니면 No

   

