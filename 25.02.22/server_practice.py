import socket, threading

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 12345))
server_socket.listen()
client, address = server_socket.accept()
print(client, address)


# client.send('connection established'.encode('utf-8'))


def recv():
    while True:
        data = client.recv(1024)
        multy = data.decode('utf-8')
        if multy == 'close':
            print('connection closed')
            break
        print('Your message: ', multy)


def send():
    while True:
        msg = input("What to say?")
        client.send(msg.encode('utf-8'))
        if msg == 'q':
            print('thanks')
            break


thread = threading.Thread(target=recv)
thread.start()
send()
server_socket.close()
