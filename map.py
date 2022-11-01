'''
filename : map.py
'''

# arr = input().split(' ')
# arr = map(int  , input().split(' '))
# print(arr)
# for i in range(len(arr)):
#     arr[i] = int(arr[i)

# for i in range(len(arr)):
#     arr[i] = arr[i] * arr[i]

# for el in arr:
#     print(el)

arr = list ( map(int, input().split(' ')) )

# def power(item):
#     return item**2

# for i in range(len(arr)):
    # arr[i] = arr[i] ** 2
# arr = map( power, arr )

# for el in arr:    
#     print(el)


##람다식으로 바꾸기.

arr = list( map( lambda item : item**2 , arr ) )

for el in arr :
    print(el)

