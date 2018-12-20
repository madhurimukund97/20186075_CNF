import socket

def main():
    host = '10.10.9.68'
    port = 1518

    s = socket.socket()
    s.connect((host,port))
    welcomemsg = s.recv(1024).decode()
    guessmsg = s.recv(1024).decode()
    guess_num = s.recv(1024).decode()
    print("Connecting to Server...\n")
    print("connected!\n")
    print(str(welcomemsg))
    print(str(guessmsg) + "\n")
    message = input("Enter your guess: ")
    while message != 'q':
        s.send(message.encode())
        data = s.recv(1024).decode()
        print(str(data))
        if guess_num == message:
            break
        message = input("Enter your guess: ")
    s.close()
if __name__ == '__main__':
    main()
