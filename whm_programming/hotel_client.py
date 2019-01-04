import socket
import time
import base64
from datetime import datetime


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8181
client.connect(('127.0.0.1', port))


def receiver_data(client):
    byte_data = client.recv(1024)
    print('Rec', byte_data.decode('utf-8'))

def send_data(client):
    for text in ['Hi server, I am 007', 'My password is 1234']:
        now = datetime.strftime(datetime.now(), '%H:%M:%S')
        msg = text + '!' + '('+now+')'
        byte_msg = bytes(msg, encoding="utf8")
        print('Send>>:', byte_msg)

        client.send(byte_msg)
        receiver_data(client)
        time.sleep(3)

send_data(client)
