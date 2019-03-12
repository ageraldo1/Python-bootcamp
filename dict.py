my_dict = {'key1':'value1', 'key2':'value2'}
print ( my_dict)
print ( my_dict['key1'])


prices_lookup = {'apple': 2.99, 'orange': 3.99, 'bananas': 1.51}
print ("Price of an orange is : {}".format(prices_lookup['orange']))

prices_lookup['strawberry'] = 0.99
prices_lookup['apple'] = 7.99

print (prices_lookup)

print ( prices_lookup.keys())
print ( prices_lookup.values())
print ( prices_lookup.items())

# more examples
student = {
    'name': 'Alex',
    'age': 40,
    'courses': ['Math', 'ComputerScience']
}

print (student)
print (student.get('phone')) # returns None

# add new key
student['phone'] = '555-55555'
print (student)

student.update({'name': 'Alex Geraldo', 'phone': '555-55555'})
print (student)   #update name field and added phone key


del student['age']
print (student)
# you can use also student.pop('age')

# looping
print (f"Total of keys   : {len(student)}")
print (f"Keys            : {student.keys()}")
print (f"Values          : {student.values()}")
print (f"Keys and Values : {student.items()}")

for k,v in student.items():
    print (f"[{k}]={v}")

