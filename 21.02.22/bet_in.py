import hashlib
FILE = 'auth.txt'
login = input('login:')
pwd = input('pwd: ')
with open (FILE, 'r') as f:
    data = f.read().split()
    if login in data:
        h = hashlib.sha224(pwd.encode('utf8')).hexdigest()
        if h == data[data.index(login)+ 1]:
            print('Authorized!')
        else:
            print('Not authorized!')
    else:
        print('login not found')