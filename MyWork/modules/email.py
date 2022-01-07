import socket
import urllib
#import htmllib2
from spiders import spider
from src import clear_src
from pathlib import Path


def email(host):
	clear_src()

	dep=spider(host)
	count=1

	with Path("email.txt").open("w+") as emails:
		if(count <int(dep)):
			s=Path("dep"+str(count)+".txt").read_text()

			for i in s:
				try:
					net=urllib.request().urlopen()
				except:
					continue

				count=count.splitlines()
				for l in str(count):
					if '@' in l:
						print(l)
						email.write(l+"\n")


	count+=1




		      


