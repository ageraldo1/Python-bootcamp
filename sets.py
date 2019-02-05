myset = set()
myset.add(1)
myset.add(2)
myset.add(2)

print ( myset)

mylist = [1,1,1,2,2,2,3,3,3,4,4,4,4,4]
print (set(mylist))  # do not allow duplicates elements

print (set('Parallel'))
print (set('Mississippi'))    # order is not preserved