import socket

def main():
	host = '10.10.9.107'
	port = 3501

	s = socket.socket()
	s.connect((host,port))

	message = input("Input: ")
	while message != "false":
		s.send(message.encode())
		data = s.recv(1024)
		print ("Recieved message: " + str(data.decode()))
		message = input("Input: ")
	s.close()

if __name__ == '__main__':
	main()