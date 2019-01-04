from datetime import datetime
import socket
import threading
import random
import base64

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8181
server.bind(('127.0.0.1', port))
server.listen(5)
print('This is server,wait for your connection...')

def handle_connect(sock,addr):
    print('Accept new connection from %s:%s...\n' % addr)
    sock.send(b'Welcome Client!')
    while True:
        msg = sock.recv(1024)
        print('Server receive the msg:', msg)
        if not msg or msg.decode('utf-8') == 'quit':
            break

        now = datetime.strftime(datetime.now(), '%H:%M:%S')
        echo = '<<: Hi,Client:' + "Good morning" + '('+now+')'+'\n'
        print('Server send echo:', echo)
        new_b_data = bytes(echo, encoding="utf8")

        sock.send(new_b_data)
    sock.close()
    print('Connection fron %s:%s closed.' % addr)

if __name__ == "__main__":
    while True:
        sock, addr = server.accept()
        t = threading.Thread(target=handle_connect, args=(sock, addr))
        t.start()

