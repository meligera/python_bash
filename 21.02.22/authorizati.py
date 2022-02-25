from getpass import getpass
import hashlib

print("Welcome to the SAFEST PASSWORD STORAGE!")
user = input("Username: ")
password = getpass().encode('utf8')
sec_u = user
sec_p = hashlib.sha224(password).hexdigest()
f = open(f"{user}.txt", 'r', encoding='utf8')
all_c = f.read()

if sec_p == all_c:
    print("Successfully authorized!")
else:
    print("Credentials not match!\n")