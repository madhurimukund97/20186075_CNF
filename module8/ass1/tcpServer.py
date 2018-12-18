import socket
def curr_to_curr(data):
    tokens = data.split(" ")
    if tokens[1] == "INR":
        if tokens[4] == "Dollar":
            return (int(tokens[2]) / 67)
        elif tokens[4] == "Pounds":
            return (int(tokens[2]) * 0.75) / 67
        elif tokens[4] == 'Yen':
            return (int(tokens[2]) * 113.41) / 67
        elif tokens[4] == 'INR':
            return tokens[2]

    if tokens[1] == "Dollar":
        if tokens[4] == "INR":
            return (int(tokens[2]) * 67)
        elif tokens[4] == "Pounds":
            return (int(tokens[2]) * 0.75)
        elif (tokens[4] == "Yen"):
            return (int(tokens[2]) * 113.41)
        elif tokens[4] == 'Dollar':
            return tokens[2]
    if tokens[1] == "Pounds":
        if tokens[4] == "INR":
            return (int(tokens[2]) * 67) / 0.75
        elif tokens[4] == "Dollar":
            return (int(tokens[2]) / 0.75)
        elif tokens[4] == "Yen":
            return (int(tokens[2]) * 113.41) / 0.75
        elif tokens[4] == 'Pounds':
            return tokens[2]
    if tokens[1] == "Yen":
        if tokens[4] == "INR":
            return (int(tokens[2]) * 67) / 113.41
        elif tokens[4] == "Dollar":
            return (int(tokens[2]) / 113.41)
        elif tokens[4] == "Pounds":
            return (int(tokens[2]) * 0.75) / 113.41
        elif tokens[4] == 'Yen':
            return tokens[2]
def main():
    host = '192.168.43.153'
    port = 3125

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    print("Server connected...!!!")
    c, addr = s.accept()
    print ("Connection established from: " + str(addr))
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print ("From connected user: " + str(data))
        data = str(curr_to_curr(data))
        
        print ("sending: " + str(data))
        c.send(data.encode())
    c.close()

if __name__ == '__main__':
    main()
