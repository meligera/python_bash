# 1) проверить високосный ли год? input от пользователя
import calendar


# k = int(input('Enter a year: '))


def cal(y):
  p = calendar.isleap(y)
  if p:
    print('Yeah..')
  else:
    print('Nah..')


# cal(k)

# 2) дана дата, дано сколько длительностью семестр, найти дату окончания семестра

import datetime


def sem(year, mon, date, leng):
  p = datetime.date(year, mon, date)
  m = datetime.timedelta(days=leng * 7)
  k = p + m
  return k.isoformat()


# print(sem(2022, 2, 10, 18))

# 3 итератор дат, приходит на вход год, месяц и список записей. Записать в файл лог с датами и записями

import os
import datetime, random


def pirate(year, mon, list_):
  f = open('log', 'w')
  c = calendar.Calendar()
  count = 0
  if count < calendar.monthrange(year, mon)[1]:
    for day in c.itermonthdays(year, mon):
      f.write("{}: {}\n".format(datetime.date(year, mon, day), random.choice(list_)))
      count += 1
      print(count)
  f.close()


# pirate(1582, 2, ["found gold at Tortuga!", "killed 2 British rats", "was in jail for a day", "there was a storm!",
# "nothing was happening", "robbed a Spanish galleon", "drank rum with crew"])


def pirate_superflex(year, mon, logs):
  def f1(y1, m1, lg):
    c = calendar.Calendar()
    iter = c.itermonthdates(y1, m1)
    count, result = 0, []
    for date, log in zip(iter, lg):
      result.append(date.isoformat() + ": " + log)
      count += 1
    return lg[count + 1:], result

  to_file = []
  while logs:
    logs, new = f1(year, mon, logs)
    to_file.extend(new)
    if mon < 12:
      mon += 1
    else:
      year += 1
      mon == 1
    f = open('logs', 'a')
    for line in to_file:
      f.write(line + "\n")


pirate_superflex(1582, 1,
                 ["found gold at Tortuga!", "killed 2 British rats", "was in jail for a day", "there was a storm!",
                  "nothing was happening", "robbed a Spanish galleon", "drank rum with crew"])
