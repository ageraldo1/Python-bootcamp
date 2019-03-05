# Counter 
from collections import Counter

my_list = [1,1,1,1,2,3,33,3,3,3,3,33,4,4,4,4,4,4,5,5,5,5,5,5]
my_string = 'aaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccc'
my_sentence = "How many many many dup dup dup is is is here here here ????"

print (Counter(my_list))
print (Counter(my_string))
print (Counter(my_sentence))
print (Counter(my_sentence.split(sep=" ")))

c = Counter(my_sentence.split(sep=" "))
print (c.most_common(2))
print ("Total of words in a sentence : {}".format(sum(c.values())))

# Defaultdict
from collections import defaultdict

# default dict
d = {'key1': 'value 1'}
print (d['key1'])

print (d['key2']) # trown an error - key not found

# now using default dict
d = defaultdict(object)
print (d['key2']) # no error - using default 

for item in d:
    print (item)

d = defaultdict(lambda: 0)
print (d['one'])
d['two'] = 2
print (d)    


# OrderedDict
d = {}

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

for k,v in d.items():
    print (k,v)

# not in order

from collections import OrderedDict

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

for k,v in d.items():
    print (k,v)


d1 = {}
d1['a'] = 1
d1['b'] = 2

d2 = {}
d2['b'] = 2
d2['a'] = 1

print (d1 == d2) # equal


d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print (d1 == d2) # not equal


# namedtuple
t = (1,2,3)
print (t[0])

from collections import namedtuple

Dog = namedtuple('Dog', 'age breed name')
eva = Dog(age=2, breed='Lab', name='Eva')
print (eva)
print (eva.age)
print (eva[0])