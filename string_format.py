print ( 'This is a string {}'.format('INSERTED'))
print ( 'The {} {} {}'.format('fox', 'brown', 'quick'))
print ( 'The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print ( 'The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))


result = 100/777
print ( result)
print ( "The result was {r}".format(r=result))
print ( "The result was {r:1.3f}".format(r=result))
print ( "The result was {r:10.3f}".format(r=result))

name = "Sam"
age = 3
print ( f'{name} is {age} years old.')
