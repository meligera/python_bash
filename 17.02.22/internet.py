import netifaces

net = netifaces.interfaces()
chose = input(f"Choose your interface: {net}")
try:
    inet = netifaces.ifaddresses(f"{net[int(chose)-1]}")[netifaces.AF_INET]
    link = netifaces.ifaddresses(f"{net[int(chose)-1]}")[netifaces.AF_LINK]
    ip = inet[0]['addr']
    mask = inet[0]['netmask']
    mac = link[0]['addr']
    print("Your ip address is:", ip)
    print("Your netmask is:", mask)
    print("Your MAC is:", mac)
except IndexError:
    print("No such interface")