'''
filename : contiue.py
'''
total = 0
score = [10,5,20,3,25]
for s in score:
    if s > 10:
        total += s 
        print(s)

total = 0
for s in score:
    if s <= 10:
        continue
    total += s 
    print(s)