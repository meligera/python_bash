import socket, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a", '--address', default='')
parser.add_argument("-p", '--port', default='')
p = parser.parse_args()
address = p.address
port = int(p.port)

try:
    client_soc = socket.socket()
    client_soc.connect((f'{address}', port))
except Exception as e:
    print("cant do that:", e)
else:
    print("connected!")
