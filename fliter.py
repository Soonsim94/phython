'''
fildname : filter.py
'''

arr = [3,2,1,10,5,7]

# for el in arr:
#     if el > 5:
#         newarr.append(el)

newarr = list( filter(lambda x : x > 5, arr ))  #람다 함수선언 
print(newarr)


