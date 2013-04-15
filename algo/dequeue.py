#!/usr/bin/env python

class Dequeue:
	def __init__(self):
		self.items = []
	def addFront(self, item):
		self.items.insert(0, item)
	def addRear(self, item):
		self.items.append(item)
	def removeRear(self):
		return self.items.pop()
	def removeFront(self):
		return self.items.pop(0)
	def isEmpty(self):
		return self.items == []
	def size(self):
		return len(self.items)

if __name__=='__main__':
	q=Dequeue()
	q.addFront(3)
	q.addFront(5)
	q.addFront(8)
	print 'size: ', q.size()
	print 'dequeue: ', q.removeFront()
	print 'isEmpty: ', q.isEmpty()