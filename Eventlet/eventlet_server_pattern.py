#!/usr/bin/env python
import eventlet

def handle(client,address):
    print 'Client ', address, ' connected'
    while True:
        c=client.recv(10000)
        if not c: break
        print c
        client.sendall(c)

server=eventlet.listen(('0.0.0.0', 6000))
pool=eventlet.GreenPool(10000)
while True:
    new_sock, address = server.accept()
    pool.spawn_n(handle, new_sock, address)
