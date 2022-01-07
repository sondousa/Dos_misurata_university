import platform 
from subprocess import call

opensys=platform.system()

def clear_src():
	if opensys=="windows":
		call('cls',shell=True)
		if opensys=="linux":
			call('clear',shell=True)