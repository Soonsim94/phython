'''
filename :  input_array.py
'''
no = input()
arr = input().split(" ")
cnt = 0
for i in arr:
    if i == no:    
        cnt += 1
print(cnt)