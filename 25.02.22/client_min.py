import socket

client_soc = socket.socket()
client_soc.connect(('127.0.0.1', 12345))
while True:
    data = client_soc.recv(1024)
    print('Received: ',data.decode('utf-8'))
    msg = input('What to send: ')
    client_soc.send(msg.encode('utf-8'))
    if msg == 'close':
        client_soc.close()
        break
