import queue
import time
import threading


def washer(dishes, dish_queue):
    for dish in dishes:
        print("Washing "+ dish + "\n")
        time.sleep(1)
        dish_queue.put_nowait(dish)

def dryer(dish_queue):
    while True:
        dish = dish_queue.get()
        print("Drying " + dish + "\n")
        time.sleep(2)
        dish_queue.task_done()

dish_queue = queue.Queue()

for n in range(2):
    dryer_thread = threading.Thread(target=dryer, args=(dish_queue,))
    dryer_thread.start()

dishes = ['salad', 'bread', 'soup', 'dessert']
washer(dishes, dish_queue)
dish_queue.join()