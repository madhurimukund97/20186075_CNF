import socket

def Main():
    host = '10.10.9.68'
    port = 3141

    server = ('10.10.9.68', 3150)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    message = input("Input: ")
    while message != "false":
        s.sendto(message.encode(), server)
        data, addr = s.recvfrom(1024)
        print("recieved : " + str(data.decode()))
        message = input("Input: ")
    s.close()

if __name__ == '__main__':
    Main()