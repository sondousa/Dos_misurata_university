import socket
from src import clear_src
from file import file 
from banner import banner
from dosattack import dos
from email import email
from spiders import spider
from ftp_server import ftp


def chosenum():
	target=input(
		"Enter Target Name.....")
	if "://" not in target:
		target=target.split("://")[1]
		return target




def main():
	while 1:
		print("")
		print("")
		print("")

		try:
                       choose=int(input("[*]Enter Number to choice...."))
                       

		except(ValueError, EOFError, KeyboardInterrupt):
                        return print("[!]Wrong Choice Please Enter Another Number.....")

		target=chosenum()
		if choice==1:
			scanner(host)

		elif choice==2:
			email(host)
		elif choice==3:
			spider(host)
		elif choice==4:
			dosattack(host)
		elif choice==5:
			ftp_server(host)
		elif choice==6:
			banner(host)

		if choice not in range(7):
			print("[!]out of Number...")



if __name__ == '__main__':
    main()



		

