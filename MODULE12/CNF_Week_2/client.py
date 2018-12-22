import socket

def main():
    host = '10.2.137.32'
    port = 1558

    s = socket.socket()
    s.connect((host,port))

    print("Connecting to Server...\n")
    print("connected!\n")

    message = str(input("Input: "))
    
    while message != 'q':
        rollnum = s.send(1024).encode()
        # s.send(message.encode())
        data = s.recv(1024).decode()
        print(str(data))
        
    s.close()
if __name__ == '__main__':
    main()
