import socket
import threading




def new_client(client, address):
    print('New: ', address)
    thread = threading.Thread(target=recv, args=(client, address))
    thread1 = threading.Thread(target=send, args=(client, address))
    thread.daemon = True
    thread1.daemon = True
    thread.start()
    thread1.start()

def recv(client, address):
    while True:
        data = client.recv(1024)
        dec = data.decode('utf-8')
        if dec == 'close':
            print('connection closed')
            client.close()
            break
        print('Your message: ', dec)


def send(client, address):
    while True:
        msg = input("What to say?")
        client.send(msg.encode('utf-8'))
        if msg == 'close':
            print('thanks')
            client.close()
            break


if __name__ == '__main__':
    server_socket = socket.socket()
    server_socket.bind(('127.0.0.1', 1995))
    server_socket.listen()
    try:
        while True:
            client, address = server_socket.accept()
            new_client(client, address)
    except KeyboardInterrupt:
        print('How rude of you\n')
        server_socket.close()
