#!/usr/bin/env python

class Stack:
    def __init__(self):
        self.items=[]

    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

if __name__=='__main__':
    s=Stack()
    print "Init stack empty?: ", s.isEmpty()
    s.push(3)
    s.push(5)
    print s.peek()
    s.pop()
    print s.pop()
