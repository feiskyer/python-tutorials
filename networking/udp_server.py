#!/usr/bin/env python
import SocketServer
import re
import sys
import socket
import struct
import fcntl
import sys

def getip(ethname):
	if ethname=="":
		ethname="eth0"
	try:
		s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		ip=socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0X8915, struct.pack('256s', ethname[:15]))[20:24])
	except:
		ip=""
	return ip

class MyUDPHandler(SocketServer.BaseRequestHandler):
	
	def handle(self):
		data = self.request[0].strip()
		socket = self.request[1]
		print "Recv from %s: %s" % (self.client_address[0],data)
		socket.sendto(data, self.client_address)

if __name__ == "__main__":
	server = SocketServer.UDPServer((getip("eth0"), 44444), MyUDPHandler)
	server.serve_forever()
