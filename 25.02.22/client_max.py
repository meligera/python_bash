import socket, argparse
import threading

parser = argparse.ArgumentParser()
parser.add_argument("-a", '--address', default='')
parser.add_argument("-p", '--port', default='')
p = parser.parse_args()

address = p.address
port = int(p.port)

client_soc = socket.socket()
client_soc.connect((f'{address}', port))


def recv():
    while True:
        data = client_soc.recv(1024)
        print('Received: ', data.decode('utf-8'))


def send():
    while True:
        msg = input('What to send: ')
        client_soc.send(msg.encode('utf-8'))
        if msg == 'close':
            client_soc.close()
            break


thread = threading.Thread(target=recv)
thread.start()
send()
