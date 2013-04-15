#!/usr/bin/env python
import re
import sys
import socket
import SocketServer
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

class MyHandler(SocketServer.BaseRequestHandler):

	def setup(self):
		self.allow_reuse_address=True
		return SocketServer.BaseRequestHandler.setup(self)

	def finish(self):
		return SocketServer.BaseRequestHandler.finish(self)

	def handle(self):
		#size=self.request.recv(4)
		buf=self.request.recv(2048).replace('\n','')
		print "Recv from %s: %s" %(self.client_address[0], buf)
		# send back message
		self.request.sendall(buf)


if __name__=='__main__':

	# start server
	server = SocketServer.ThreadingTCPServer( (getip("eth0"),44444), MyHandler)
	server.serve_forever()
