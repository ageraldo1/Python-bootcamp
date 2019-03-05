import datetime

my_time = datetime.time(5,25,1)
print (my_time)
print (my_time.hour)

print (datetime.time.min)
print (datetime.time.max)

today = datetime.date.today()
print (today)
print (today.timetuple())
print (today.year)

d1 = datetime.date(2019,3,15)
print (d1)

d2 = d1.replace(year=2015)
print (d2)

print ( d1 - d2)
d3 = d1 - d2
print (type(d3))
