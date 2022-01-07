from src import clear_src
import urllib
import re
from pathlib import Path



def spider(host):
	clear_src()

	print("[*] Use the result to find promising URLs/Emails to try hacking using SQL injection or Xss or Social Engineering etc.\n[*] Depth is the level to go inside the website( usually a small integer ).\n[*] Output will also be saved in text files in the same folder as this software.\n")
	depth=input("Enter....")
	count+=1
	href_pattern=re_compile('''href=["'](.[^"']+)["']''')
	url="http://"+host
	with path(f"depth1.txt").open('w') as out_file:
		for i in href_pattern.findall(str(urllib.request.urlopen()),re,I):
			if "http" not in i:
				i="http://"+host+i
				print(i)
				out_file.write(i+'\n')

	while(count<int(depth)):
		with Path("depth"+str(count)+".txt").open()as read_file:
			read = read_file.read().splitlines()
			if not read:
				print("\n *******finish************")

		for link in read:
			if "http" not in link:
				link="http://"+host+link

				try:
					for k in href_pattern.findall(str(urllib.request.urlopen(link).read()).re,I):
						print(k)

						write_file.write(k+"\n")

				except:
					continue
		count+=1

	return depth



