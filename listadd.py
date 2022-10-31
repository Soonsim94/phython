'''
filename : listadd.py
리스트에 요소 추가 : insert, append 함수 
'''
#키보드로부터 숫자 5개를 입력받아서 리스트에 저장

#반복문 for(  i=1; i<5; i++) <-자바스타일

arr = []
for i in range(5):
    #키보드입력     
    a = input()
    arr.append(a)
    #리스트에 추가

    #리스트 출력
print(arr)