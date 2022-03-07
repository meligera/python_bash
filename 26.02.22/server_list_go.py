import socket

f = open('one_by_one', 'r')
lines = f.readlines()
book = []
for line in lines:
    book.append(line.strip('\n'))

print(book)


def check_ip(i):
    if not i.count('.') == 3:
        print('not valid IP')
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
            client_soc = socket.socket()
            print('checking address:', ip)
            temp = []
            str_ip = str(ip)
            if ':' not in str_ip:
                str_ip += ':22'
            temp.append(str_ip.split(':'))
            client_soc.settimeout(2)
            status = client_soc.connect_ex((f'{temp[0][0]}', int(temp[0][1])))
            result_dict[ip] = status
            print('it says:', status, '\n')
        else:
            print('impossible to proceed \n')
    for ip in result_dict.keys():
        out = 'OK \u2713' if result_dict[ip] == 0 else 'NOT OK \u2717'
        kawai = len(ip)
        # print(ip + '{0:>50}'.format(out))
        k = 70 - kawai
        print(f"{ip:>1}{out:>{k}}")


ping_ips(book)
