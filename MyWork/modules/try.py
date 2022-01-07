import socket
from datetime import datetime
import random
from src import clear_src
from useragent import user_agents


def dos(host):
    clear_src()

    ip=socket.gethostbyname(host)
    conn=int(input("Ente number of port"))
    for i in range(conn):
        try:
           s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
           
           except:
               print("")
               continue
            
         
                     
             
             
