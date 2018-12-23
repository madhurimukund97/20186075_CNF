import socket
import os, signal, time
from threading import *

def main():
    host = '192.168.137.236'
    port = 5006

    s = socket.socket()
    s.bind((host,port))

    print('server connected...')
    s.listen(20)

    
    mult_clients = []
    user_names = {}

    while True:
        c, addr = s.accept()
        welcome = "Welcome!!!!"
        c.send(welcome.encode())
        c.send('\nUser_name: '.encode())
        conn_name = c.recv(1024)
        user_names[c] = str(conn_name.decode())
        mult_clients.append(c)
        for con in mult_clients:
            if c != con:
                con.send((user_names[c] + ' is Connected.').encode())
        Thread(target = clientchat, args = (c, addr, mult_clients, user_names)).start()
    s.close()

def clientchat(cl, addr, mult_clients, user_names):
    while True:
        message = (cl.recv(1024)).decode()
        print(user_names[cl] + ' ----msged--- ' + message)
        if message == 'Bye' and cl not in mult_clients:
            for client in mult_clients:
                if cl != client:
                    name = user_names[cl]
                    client.send((name + '----msged---' + message).encode())
    cl.close()


if __name__ == '__main__':
    main()
