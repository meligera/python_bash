import pwd, os, argparse, time
import threading
from threading import Timer

name = pwd.getpwuid(os.getuid()).pw_name
print(f"Welcome {name.capitalize()}! We are so glad to see you! \n")

parser = argparse.ArgumentParser()
parser.add_argument("-s", '--source', default='')
parser.add_argument("-o", '--output', default='')
d = parser.parse_args()
extension = os.path.splitext(d.source)[1]

if os.path.isdir(f"{d.output}"):
    print("Checking if folder is present...    OK")
    time.sleep(0.8)
else:
    print("Checking if folder is present... Error")
    print("Thank you for using us!")
    quit()
if os.path.exists(f"{d.source}"):
    print("Checking if file is present...      OK")
    time.sleep(0.8)
else:
    print("Checking if file is present... Error")
    print("Thank you for using us!")
    quit()
if os.path.isfile(f"{d.source}"):
    print("Checking if file is suitable...     OK")
    time.sleep(0.8)
else:
    print("Checking if file is suitable... Error")
    print("Thank you for using us!")
    quit()
if extension == ".txt":
    print("Checking if file is supported...    OK")
    time.sleep(0.8)
else:
    print("Checking if file is supported... Error")
    print("Thank you for using us!")
    quit()

stop_thread = False


def ask():
    os.system("clear")
    print("No more time left, master!\n")
    print(f"Be more certain, {name.capitalize()}!")
    os._exit(0)


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = 'You have: {:02d} seconds left'.format(secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        global stop_thread
        if stop_thread:
            break


timm = Timer(10.0, ask)
timer_thread = threading.Thread(target=countdown, args=(10,))
count_thread = threading.Thread(target=timm.start(), args=())
timer_thread.start()
count_thread.start()

inpy = input("Are you sure you wanna do it?\n")

if inpy != "y":
    os.system("clear")
    print("Did nothing, sad...\n")
    print(f"Thank you for using me ^^, {name.capitalize()}!")
    timm.cancel()
    stop_thread = True
else:
    timm.cancel()
    stop_thread = True
    with open(f"{d.source}") as file:
        lines = [line.rstrip() for line in file]
        for line in lines:
            os.system(f"touch {d.output}{line}.txt")
        os.system("clear")
        print(f"Good job, {name.capitalize()}! I've created {len(lines)} files. At {d.output} \n")
        print("Thank you for choosing me~~ UwU!")
