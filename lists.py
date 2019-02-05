my_list = [1, 2, 3]
my_mixed_list = ["STRING", 100, 2.3]

print ( my_list)
print ( my_mixed_list)

print ("Size of the list : {}".format(len(my_list)))

first_list  = ['one', 'two', 'three']
second_list = ['four', 'five', 'six']

new_list = first_list + second_list

print ( "My new list is : {}".format(new_list))


new_list[0] = new_list[0].upper()    # list is mutable
new_list.append('seven')
print ( "My new list is : {}".format(new_list))

num_list = [1,29,3,7, 19, 10, 0, -10, 399]
num_list.sort()
print ( num_list)

num_list.reverse()
print ( num_list)
