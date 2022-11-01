

def mymin(*nums):
    min = nums[0]
    for num in nums:
        if min > num:
            min = num
    return(min)




result = mymin(3,5,10,2)
print(result)
