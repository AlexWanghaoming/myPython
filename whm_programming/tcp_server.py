import socket
import sys
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 5000
sk.bind((host, port))

sk.listen(1)

while 2:
    clint, addr = sk.accept()
    print("clint address:{}".format(addr))
    while True:
        data = clint.recv(10)
        print(data)
        if not data:
            sys.exit()
        print("going to run cmd:{}".format(data))
