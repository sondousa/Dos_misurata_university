from src import clear_src
import socket
import urllib
import struct
import httplib2
from useragnet import user_agents
from datetime import datetime
import struct
from ipaddress import ip_address, ip_network



def scanner(host):
	clear_src()
	print("Choose the type of scan from 1 to 7:")
	print("1. Full Port Scan(1-65535) \n2. Specific port range\n3. Single Port \n4. Most popular ports")
	type=int(input("Enter Type of scan:"))
	s=socket(socket.AF_INET,socket.SOCK_DGRM)
	target_url=input("Enter URL:")

	if type==1:
		ip_addr = socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', inter[:15]))[20:24])
		print(ip_addr)
		
	elif type==2:
		grabber=httplib2.build.opner()
		garbber.addheaders=(useragnets())
		try:
			ip_address=grabber.open(target_url).read()
		except httplib2.HTTgPError.error:
			print("There was an error trying to get your Public IP: %s") % (error)
		except httplib2.URLError.error:
			print("There was an error trying to get your Public IP: %s") % (error)

		print(ip_address)

	elif type==3:
		port1=int(input("Enter Port:"))
		port2=int(input("Enter Port"))
		port2+=1
	    ports=list(range(port1,port2))
	        

    elif type==4:
	ports=[]
	ports.append(int(input("Enter port")))

	elif type==5:
		porst=[80,443,21,22]
		
	elif type==6:
		print("this is ports::")
	    t1=datetime.now()
	    print(""+host)
	    print(""+str(t1))
	    host=socket.gethostbyname(host)
	    print(""+host)
	    for port in ports:
	    	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		    result=sock.connect_ex((host,port))
		    if result==0:
		    	print("port{}: /t open.format(port")
			    sock.close()
			    clear_src()

	elif type==7:
		sender=socket.socket(socket.AF_INET,socket.SOCK.SOCK_DGRM)
		for ip in ip_network(host).hosts():
			sender.sendto(message.encode('utf-8'),(str(ip),65212))


	class IP(Structure):
		_fields_ = [
        ("ihl", c_ubyte, 4),
        ("version", c_ubyte, 4),
        ("tos", c_ubyte),
        ("len", c_ushort),
        ("id", c_ushort),
        ("offset", c_ushort),
        ("ttl", c_ubyte),
        ("protocol_num", c_ubyte),
        ("sum", c_ushort),
        ("src", c_uint32),
        ("dst", c_uint32)
    ]

     def __new__(cls, socket_buffer=None):
        return cls.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):
        self.socket_buffer = socket_buffer


    # map protocol constants to their names
    self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}

    # human readable IP addresses
    self.src_address = socket.inet_ntoa(struct.pack("@I", self.src))
    self.dst_address = socket.inet_ntoa(struct.pack("@I", self.dst))

    try:
    	self.protocol=self.protocol_map[self.protocol_num]
    except IndexError:
    	self.protocol=str(self.protocol_num)

    class ICMP(Structure):
    _fields_ = [
        ("type", c_ubyte),
        ("code", c_ubyte),
        ("checksum", c_ushort),
        ("unused", c_ushort),
        ("next_hop_mtu", c_ushort)
    ]

     def __new__(cls, socket_buffer=None):
        return cls.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):
        self.socket_buffer = socket_buffer








		









