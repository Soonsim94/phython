'''
제일 큰수 찾는 함수
매개변수 : 정수형값들 
리턴값 : 정수형 
'''

def mymax(*nums):
    #결과(제일큰수)를 지정할 변수에 첫번째 요소로 초기화.
    max = nums[0]
    #리스트 수만큼 반복
    for m in nums:
        #리스트 수만큼 반복하면서 큰수인지 검사함.
        if m > max:
            #리스트 값이 크다면 변수에 저장.
            max = m    
    # 결과를 리턴 
    return max

result = mymax(3,5,10,2)
print(result)

result = mymax(100,50)
print(result)





    


# t = mysum(10,20)
# print(t)
# print( mysum(10,20,30) )
# print( mysum(10,20,3,3,4,5,5,5,6) )






