import socket

def Main():
	host = '10.10.9.68'
	port = 5003

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))

	print ("Server started....")
	while True:
		data, addr = s.recvfrom(1024)
		print("message : " + str(addr))
		print("from: " + str(data.decode()))
		data = str(data.decode()).upper()
		print("sending: " + str(data))
		s.sendto(data.encode(), addr)
	s.close()

if __name__ == '__main__':
	Main()

