#!/usr/bin/env python
# inst.eecs.berkeley.edu/~cs61a/sp12/hw/hw1.html
# Q4. Douglas Hofstadter’s Pulitzer-prize-winning book, Gödel, Escher, Bach, poses the following mathematical puzzle.
# 
# Pick a positive number n
# If n is even, divide it by 2.
# If n is odd, multipy it by 3 and add 1.
# Continue this process until n is 1.
# The number n will travel up and down but eventually end at 1 (at least for all numbers that have ever been tried -- nobody has ever proved that the sequence will always terminate).
# 
# The sequence of values of n is often called a Hailstone sequence, because hailstones also travel up and down in the atmosphere before falling to earth. Write a function that takes a single argument with formal parameter name n, prints out the hailstone sequence starting at n, and returns the number of steps in the sequence:

l=[]
def f(n):
	l.append(n)
	if n==1:
		return
	if n%2==0:
		n=n/2
	else:
		n=n*3+1
	f(n)

if __name__=='__main__':
	import sys
	if len(sys.argv)!=2:
		print('Usage: %s num'% sys.argv[0])
		sys.exit(1)
	f(int(sys.argv[1]))
	print(l)
