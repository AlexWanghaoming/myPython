import socket
import sys
s = socket.socket()

s.connect(('127.0.0.1', 5000))

while 1:
    cmd = input('please input cmd:')
    if cmd == 'quit':break
    elif cmd == '':
        continue
    s.sendall(bytes(cmd, encoding="utf8"))
    data = s.recv(2048)
    print(data)

s.close()
