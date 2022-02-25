# ряд чисел нужно посчитать все степени до limit и записать в файлы f(x, limit=10) pows_2.txt - 1, 2, 4, 8, 16, 32...

def multik(x, limit):
  li = []
  for i in range(1, limit+1):
    li.append(pow(x, i))
  f = open(f'pows_{x}.txt', 'a')
  for b in li:
    f.write(str(b) + "\n")

multik(2, 10)

import time, multiprocessing
t_first = time.time()
for i in range(2, 20):
  multik(4, 100)
t_second = time.time()
print("Simple", t_second-t_first)
for i in range(2, 20):
  p = multiprocessing.Process(target=multik, args=(4, 100),)
  p.start()
t_third = time.time()
print("Multiproc", t_third-t_second)
