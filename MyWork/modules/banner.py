import socket
from src import clear_src

def banner(host):
	clear_src()

	
	try:
		s=socket.socket(socket.AF_INET,socket.SCOK_STREAM)
	except:
		"ERROR"
		host=socket.gethostbyname(host)
		port=int(input("Enter the port of the services:"))
		try:
			s.connect((host,port))
			print("[*")
			if port==80:
				msg="HEAD/HTTP"
				msg=msg.encode()
				s.send(msg)
			data=s.recv(1024)
			print("==============>"+data.decode())
			s.close()
		except Exception as e:
			print(e)
