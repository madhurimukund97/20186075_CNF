import socket

def Main():
	host = '10.10.9.68'
	port = 5004

	server = ('10.10.9.68', 5003)

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))

	message = input("Input: ")
	while message != "false":
		s.sendto(message.encode(), server)
		data = s.recv(1024)
		print("recieved : " + str(data.decode()))
		message = input("Input: ")
	s.close()

if __name__ == '__main__':
	Main()