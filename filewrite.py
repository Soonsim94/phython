'''
filename : filewrite.py
'''

users = [ { 'userno':100, 'username':'user1', 'salary':2000},  
          { 'userno':101, 'username':'user2', 'salary':1000}, 
          { 'userno':102, 'username':'user3', 'salary':1500}]


#파일오픈
file = open('d:/basic.txt','w')
#쓰기
for el in users:
    file.write(f'{el["userno"]} {el["username"]} {el["salary"]}\n')

#닫기
file.close()



