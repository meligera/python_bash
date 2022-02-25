# написать программу принимает список имён файлов, что заменить на что заменить
# 1) последовательный или 2) процессы s =f.read(); s.replace(text1, text2)
from random import randrange
import multiprocessing

def replace():
  for o in range(1, 15):
    with open(f'replace_{o}.txt', 'r') as file:
      filedata = file.read()
    filedata = filedata.replace('Tom', 'German')
    filedata = filedata.replace('Garry', 'German')
    filedata = filedata.replace('Michael', 'German')
    filedata = filedata.replace('Harry', 'German')
    with open(f'replace_{o}.txt', 'w') as file:
      file.write(filedata)
    file.close()
    o += 1


names = ["Tom", "Garry", "Michael", "Harry"]
verbs = "is"
nouns = "the best"


def gen():
  for o in range(1, 15):
    f = open(f'replace_{o}.txt', 'a')
    for i in range(0, 300):
      f.write((names[randrange(0, len(names))] + " " + verbs + " " + nouns) + "\n")
    f.close()

mas = []

def proc(mas):
  for m in mas:
    g = multiprocessing.Process(target=gen(), args=(),)
    g.start()
    r = multiprocessing.Process(target=replace(), args=(),)
    r.start()

for i in range(2, 200):
  mas.append(f"replace_{i}")

proc(mas)
