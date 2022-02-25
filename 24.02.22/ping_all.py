import ipaddress, sys
import subprocess

f = open('pingy', 'r')
lines = f.readlines()
book = []
for line in lines:
    book.append(line.strip('\n'))


def check_ip(i):
    if not i.count('.') == 3:
        print('im here3')
        return False
    port = 0
    each = i.split('.')
    if ':' in each[-1]:
        new, port = each.pop().split(':')
        each.append(new)
    try:
        port = int(port)
        int_map = map(int, each)
        int_list = list(int_map)
        for num in int_list:
            if num > 255 or num < 0:
                print(f'not valid number: {num} in ip: {i}')
                return False
            if port < 0 or port > 65535:
                print(f'port name is invalid: {port}')
                return False
    except ValueError:
        print("we take numbers only")
        return False
    return True


def ping_ips(ips):
    result_dict = dict()
    for ip in ips:
        if check_ip(ip):
            status = subprocess.call(['ping', '-c5', ip])
            result_dict[ip] = status
        else:
            print('impossible to proceed')
    for ip in result_dict.keys():
        out = 'OK \u2713' if result_dict[ip] == 0 else 'NOT OK \u2717'
        kawai = len(ip)
        # print(ip + '{0:>50}'.format(out))
        k = 70 - kawai
        print(f"{ip:>1}{out:>{k}}")


ping_ips(book)
