import socket

def Main():
	host = '10.10.9.68'
	port = 3120

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
		data = str(data).upper()
		print ("sending: " + str(data))
		c.send(data.encode())
	c.close()

if __name__ == '__main__':
	Main()