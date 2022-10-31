'''
filename : range.py
특정한 횟수만큼 반복

11 -0 11-i
9 -1
7 -2
5 -3
'''

#1~10

# for i in range(0,11):    #range(1부터,10까지출력,증가범위(사이간격수(홀수))) ex)range(1,10,2)
#     print("*"*i)
#     print(" " * ( (11-i)//2), "*"*i)


#0~10짝수
n=int(input())

for i in range(1,n+1):
    #공백출력
    for j in range(n-i):
        print(" ", end="")
    #별출력
    for j in (range(i)):   
        print("*", end="")
    print()


#감소 

output = ""

for i in range(1,n+1):
    #공백출력
    for j in range(n-i):
        output += " "
    #별출력
    for j in range(i):
        output += "*"
    output += '\n'
print(output)