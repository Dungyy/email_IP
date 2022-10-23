from urllib.request import urlopen
import re

# SETUP where to look for IP 
url = 'http://checkip.dyndns.com'

# OPen url and print out IP

request = urlopen(url).read().decode('utf-8')

ourIP = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", request)
ourIP = str(ourIP)

print("Our IP address is: ", ourIP)
