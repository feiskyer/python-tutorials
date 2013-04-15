#!/usr/bin/env python

class Queue:
	def __init__(self):
		self.items = []
	def enqueue(self, item):
		self.items.insert(0, item)
	def dequeue(self):
		return self.items.pop()
	def isEmpty(self):
		return self.items == []
	def size(self):
		return len(self.items)

if __name__=='__main__':
	q=Queue()
	q.enqueue(3)
	q.enqueue(5)
	q.enqueue(8)
	print 'size: ', q.size()
	print 'dequeue: ', q.dequeue()
	print 'isEmpty: ', q.isEmpty()