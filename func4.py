'''
filename : func4.py
가변매개변수 (*)

tuple :()  list와 동일하고 요소 변경 불가.
list : []  요소 변경 가능.
'''
'''
설명 : 합계계산 
매개변수 : 정수형값 가짐 여러개.
리터값 : 정수형 합계를 넘겨주고있음.    어떤값을 불러오고 어떤값을 넘겨받나
'''

def mysum(*nums):
    total = 0
    # print(type(num))
    for num in nums:
        total += num
    # print(total)
    return total
    

t = mysum(10,20)
print(t)
print( mysum(10,20,30) )
print( mysum(10,20,3,3,4,5,5,5,6) )

