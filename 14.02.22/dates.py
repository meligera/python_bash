import datetime, calendar
c = calendar.Calendar()
for day in c.itermonthdays(1592, 8):
  print(day)
