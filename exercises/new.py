import socket
import sys


# def connect_to_ip(ip, port):
#     try:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.connect((ip, port))
#         return sock
#
#     except Exception:
#         return None
# def scan_port(ip, port, timeout):
#     socket.setdefaulttimeout(timeout)
#     sock = connect_to_ip(ip, port)
#
#     if sock:
#         print('Able to connect to: {0}:{1}').format(ip, port)
#         sock.close()
#     else:
#         print('Not able to connect to: {0}:{1}').format(ip, port)
# # Get the IP / domain from the user
# ip_domain = raw_input("Enter the ip or domain: ")
# if ip_domain == '':
#     print('You must specify a host!')
#     sys.exit(0)
#
# # Get the port range from the user
# port = raw_input("Enter the port range (Ex 20-80): ")
# if port == '':
#     print('You must specify a port range!')
#     sys.exit(0)
#
# # Optional: Get the timeout from the user
# timeout = raw_input("Timeout (Default=5): ")
# if not timeout:
#     timeout = 5
# port_range = port.split("-")
#
#
# # Get the IP address if the host name is a domain
# try:
#     ip = socket.gethostbyname(ip_domain)
# except Exception:
#     print('There was an error resolving the domain')
#     sys.exit(1)
#
# # If the user only entered one port we will only scan the one port
# # otherwise scan the range
# if len(port_range) < 2:
#     scan_port(ip, int(port), int(timeout))
# else:
#     for port in range(int(port_range[0]), int(port_range[1])+1):
#         scan_port(ip, int(port), int(timeout))
#

# import re
# class PortScanner():
#     def __init__(self,timeout=5):
#         print (">>>",end="")
#         self.ip_or_domain=input("Enter Your Domain or Ip address: ")
#         try:
#             self.ip = socket.gethostbyname(self.ip_or_domain)
#         except Exception:
#             print ("Unable to resolve hostname {}".format(self.ip_or_domain))
#             sys.exit(1)
#         print (">>>",end="")
#         self.port=input("Please enter your Port range (20-80): ")
#         self.port_range=re.split(',|:|-',self.port)
#         print(">>>", end="")
#         self.timeout = timeout
#
#
#     def connect_to_ip(self,in_port):
#         try:
#
#             sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#             sock.connect((self.ip,int(in_port)))
#             return sock
#         except Exception:
#             return None
#     def scan_port(self,in_port):
#         socket.setdefaulttimeout(int(self.timeout))
#         sock=self.connect_to_ip(in_port)
#         if sock:
#             print ("Able to Connect: {0}:{1}".format(self.ip,in_port))
#             sock.close()
#         else:
#             print("Unable to Connect: {0}:{1}".format(self.ip, in_port))
#
# checkport=PortScanner()
# if len(checkport.port_range)<2:
#     checkport.scan_port(checkport.port_range[0])
# else:
#     for i in range(int(checkport.port_range[0]),int(checkport.port_range[1])+1):
#         checkport.scan_port(i)
#

import urllib2
from urllib2 import urlopen
import json
import re

# Get Public IP


def getPublicIP():
    data = str(urlopen('http://checkip.dyndns.com/').read())
    return re.compile(r'Address: (\d+.\d+.\d+.\d+)').search(data).group(1)

IP = str(getPublicIP())

# Get Location
url = 'http://ipinfo.io/' + IP + '/json'
response = urlopen(url)
data = json.load(response)
city = data['city']
region = data['region']
country = data['country']
location = data['loc']
org = data['org']

# Print Extracted Details
print "Your City : " + city
print "Your Region : " + region
print "Your Country : " + country
print "Your Location : " + location