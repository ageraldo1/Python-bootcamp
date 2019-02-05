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