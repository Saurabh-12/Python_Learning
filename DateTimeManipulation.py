from datetime import datetime

d = datetime.now() #today's datetime
print("today's datetim: ",d)

print("day of week - Monday is 0 and Sunday is 6")
print(d.weekday()) #day of week - Monday is 0 and Sunday is 6
print("Year: ",d.year)
print("Month: ",d.month)
print("Day: ",d.day)
print("Hour: ",d.hour)
print("Minute: ",d.minute)
print("Second: ", d.second)

print(d.strftime("%A %d/%m/%Y")) # date to string

date_string = '2020-02-01 12:00PM'
print(datetime.strptime(date_string, '%Y-%m-%d %I:%M%p'))

date_string = '02/01/2020'
d = datetime.strptime(date_string, '%m/%d/%Y')
print(d)

from datetime import timedelta
d1 = datetime.now()
date_string = '2/01/2016'
d2 = datetime.strptime(date_string, '%m/%d/%Y')
print(d1 - d2)