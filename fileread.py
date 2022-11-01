'''
filename : fileread.py
'''

#open
with open('d:/basic.txt', 'r') as file:  #저장된 메모장파일 내에 있는 문서 읽혀줌. 
    #한 줄씩 처리
    liens = file.readlines() 
    for line in liens:
        info = line.split(" ")
        print(info[1])
