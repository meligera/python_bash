import string
f = open('source.txt', 'a')
for i in range(100000):
    f.write(string.ascii_letters)
f.close()