import socket
server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 12345))
server_socket.listen()
client, address = server_socket.accept()
print(client, address)
client.send('connection established'.encode('utf-8'))
while True:
    data = client.recv(1024)
    multy = data.decode('utf-8')
    if multy == 'close':
        print('connection closed')
        break
    mul = int(multy)
    fin = mul**2
    print('Your message: ', fin)
    client.send(str(fin).encode('utf-8'))

server_socket.close()