
users = [ { 'userno':100, 'username':'user1', 'salary':2000},  
          { 'userno':101, 'username':'user2', 'salary':1000}, 
          { 'userno':102, 'username':'user3', 'salary':1500}
]

#급여로 필터값 알고싶을때 
arr = list( filter( lambda item : item['salary']>1000 ,users))
nos = list( map( lambda item : item['userno'] , arr ) )
print(nos)

