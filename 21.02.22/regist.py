from getpass import getpass
import hashlib

print("Welcome to the SAFEST PASSWORD STORAGE!")
user = input("Username: ")
password = getpass().encode('utf8')


def valid_pwd(pwd):
    b, l, d = False, False, False
    long = len(pwd) >= 8
    for sym in pwd:
        if sym.isupper(): b = True
        if sym.islower(): l = True
        if sym.isdigit(): d = True


def valid_lo(fn, login):
    with open(fn, 'r') as f:
        return not login in f.read()


sec_p = hashlib.sha224(password).hexdigest()
sec_u = user
f = open(f"{user}.txt", 'w', encoding='utf8')
f.write(f"{sec_p}")
f.close()
