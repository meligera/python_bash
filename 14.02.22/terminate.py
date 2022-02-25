import calendar
import multiprocessing
import time

def count(time_sleep):
  for i in range(10000):
    print("Counter is:", i)
    time.sleep(time_sleep)

process = multiprocessing.Process(target=count, args=(1,))
process.start()
time.sleep(5)
process.terminate()
