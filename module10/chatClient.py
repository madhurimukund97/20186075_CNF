import socket
from threading import *
import os,signal

def Main():
    host = '192.168.137.236'
    port = 5006

    s = socket.socket()
    s.connect((host, port))
    start = Thread(target = send, args = (s,)).start()

    while True:
        data = s.recv(1024).decode()
        print(data)
def send(s):
    while True:
        msg = input()
        s.send(msg.encode())

if __name__ == '__main__':
    Main()