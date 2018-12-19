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
        elif tokens[4] == "Yen":
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
def Main():
    host = '10.10.9.68'
    port = 3150

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print ("Server started....")
    while True:
        data, addr = s.recvfrom(1024)
        print("message : " + str(addr))
        print("from: " + str(data.decode()))
        data = str(curr_to_curr(data.decode()))
        print("sending: " + str(data))
        s.sendto(data.encode(), addr)
    s.close()

if __name__ == '__main__':
    Main()

