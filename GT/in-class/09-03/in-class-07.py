def average(nums):
    if len(nums) > 0:
        return (sum(nums)/len(nums))
        
    else:
        return 0

print(average([2,2,2,2]))
print(average(range(1,30)))
print (average(list()))