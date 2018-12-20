import socket
import random

def main():
    host = '10.10.9.68'
    port = 5013

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)
    print("Server connected....")
    c, addr = s.accept()
    print("connection from: " + str(addr))
    welcomemsg = "Welcome!!!!"
    guessmsg = "Within less attempts guess a number between 1 and 50"
    c.send(welcomemsg.encode())
    c.send(guessmsg.encode())
    guess_number = random.randint(1,50)
    c.send(str(guess_number).encode())
    guess_count = 0
    while True:
        data = c.recv(1024).decode()
        print("Guess: " + str(data))
        if not data:
            break
        if int(data) == guess_number:
            guess_count += 1
            output = "Correct, number of guess: " + str(guess_count)
            c.send(output.encode())
            break
        elif int(data) < guess_number:
            guess_count += 1
            output = "Enter high value"
            c.send(output.encode())
        elif int(data) > guess_number:
            guess_count += 1
            output = "enter low value"
            c.send(output.encode())
        
    c.close()
if __name__ == '__main__':
    main()
