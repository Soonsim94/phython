'''

'''

#list
names = [ '김', '이', '박']

print("list===")
for obj in names:
    print(obj)


#list range
print("list range===")
for idx in range(len(names)):
    print(names[idx])

#dictionary
dict = {'no':100, 'username':'user1','salary':2000 }

print("dict====")
for key in dict:
    print(key, dict[key])

print("dic items=====")
for key,value in dict.items():
    print(key,value)


users = [ { 'no':100, 'username':'user1', 'salary':2000},   #객체값 
          { 'no':101, 'username':'user2', 'salary':1000}, 
          { 'no':102, 'username':'user3', 'salary':1500}]

print("list dict====")   #user의 객체값을 불러오는것 객체안에 있는 username을 찾는다 / 중괄호를 가져온것. 좀 더 세부적
for obj in users:
    print(obj["username"])

print('list dict range====')  #user 방을 가져오는것. 0번방 하나.
for idx in range(len(users)):
    print(users[idx]['username'])   

#급여 합계 구하기
total = 0
for s in users:
    total += s['salary']
print(total)     #한번만 할거면 내어쓰기! 여러번은 들여쓰기

#최대급여와 최소급여

maxSalary = users[0]['salary']
minSalary = users[0]['salary']

for obj in users:
    if obj['salary'] > maxSalary: 
        maxSalary = obj['salary']  
    if obj['salary'] < minSalary: 
        minSalary = obj['salary'] 
print('최대', maxSalary) 
print('최소', minSalary) 


