import hashlib
FILE = 'auth.txt'
def valid_pwd(pwd):
    b, l, d = False, False, False
    long = len(pwd) >= 8
    for sym in pwd:
        if sym.isupper(): b = True
        if sym.islower(): l = True
        if sym.isdigit(): d = True
    return b and l and d and long

def valid_lo(fn, login):
    with open(fn, 'r') as f:
        return not login in f.read()


login = input('login: ')
while not valid_lo(FILE, login):
    login = input('Login exists\n login:')

pwd = input("pwd: ")
counter = 0
while not valid_pwd(pwd) and counter < 3:
    pwd = input("pwd: ")
    counter += 1
pwd_hash = hashlib.sha224(pwd.encode('utf8')).hexdigest()
with open (FILE, 'a') as f:
    f.write('ln' + ' ' + login + ' ' + pwd_hash + ' ')