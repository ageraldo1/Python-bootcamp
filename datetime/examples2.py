import datetime

d = datetime.date(2019,3,4)
t = datetime.date.today()

print (d)
print (t)

tdelta = datetime.timedelta(days=7)
print (t + tdelta)
print (t - tdelta)

# When 
#   add/sub date and timedelta => date
#   add/sub date and date      => timedelta

bday = datetime.date(2019,7,1)
till_bday = bday - t
print (till_bday.days)
print (till_bday.total_seconds())



# time
t = datetime.time(9,30,45)
print (t)
print (t.hour)

# datetime
dt = datetime.datetime(2019, 3, 4, 21, 30, 45)
print (dt)
print (dt.date())
print (dt.time())

tdelta = datetime.timedelta(days=7)
print ( dt + tdelta)

tdelta = datetime.timedelta(hours=1)
print ( dt + tdelta)


# more examples
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print (dt_today)
print (dt_now)
print (dt_utcnow)


# pytz
import pytz

dt = datetime.datetime(2019, 3, 4, 21, 57, tzinfo=pytz.UTC)
dt_now = datetime.datetime.now(tz=pytz.UTC)
print (dt)
print (dt_now)

dt_est = dt_now.astimezone(pytz.timezone('US/Eastern'))
dt_mnt = dt_now.astimezone(pytz.timezone('US/Mountain'))
print (dt_est)
print (dt_mnt)

for tz in pytz.all_timezones:
    print (tz)


# notimezone
no_tz = datetime.datetime.now()
tz_est = pytz.timezone('US/Eastern')
yes_tz = tz_est.localize(no_tz)

print (no_tz)    
print (yes_tz)

dt_est = datetime.datetime.now(tz=pytz.timezone('US/Eastern'))
print (dt_est.isoformat())
print (dt_est.strftime("%B %d, %Y"))

dt_str = "March 04, 2019"
dt = datetime.datetime.strptime(dt_str, "%B %d, %Y")
print (dt)
