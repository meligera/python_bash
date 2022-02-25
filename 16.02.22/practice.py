# вывести все файлы из директории сортированные по дате 1.1) вывести info в приемлемом виде; 1.2) выделить info из даты
# 1.3) сортировка

# Удалить повторяющиеся файлы-дубликаты из директории. Есть две директории удаляем дубликаты 2.1) научится находить
# повторяющееся файлы, 2.2) написать программу удаления

import os, filecmp
from datetime import datetime


def info(name):
  inf = os.stat(name)
  result = ""
  result += f"Path: {os.getcwd()}/{name} \n"
  result += f"uid: {inf.st_uid} \n"
  result += f"gid: {inf.st_gid} \n"
  result += f"Size: {inf.st_size} \n"
  t = datetime.utcfromtimestamp(inf.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
  result += f"Modified: {t} \n"
  return result


def sort_file(d):
  list_files = os.listdir(d)
  dict_file = {}
  for f in list_files:
    time = (os.stat(f)).st_mtime
    dict_file[f] = time
  items = dict_file.items()
  items = sorted(items, key=lambda x: x[1])
  for fn, t in items:
    print(fn, datetime.utcfromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S'))


def rep(dir1, dir2):
  l = filecmp.dircmp(dir1, dir2)
  for file in l.same_files:
    f = open(dir1+'/'+ file, 'r')
    f1 = open (dir2+'/'+ file, 'r')
    s1, s2 = f.read(), f1.read()
    if hash(s1) == hash(s2):
      q = str(input(f"Where to remove the duplicate: {dir1} or {dir2}?"))
      if q == "1":
        path = dir1
        os.remove(path + "/" + file)
        quit()
      elif q == "2":
        path = dir2
        os.remove(path + "/" + file)
        quit()

rep("asia", "africa")
