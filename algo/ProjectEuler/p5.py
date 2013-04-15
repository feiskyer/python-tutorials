# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?

def gcd1(m,n): #greatest common divisor
    while m!=n:
        if m>n:
            m=m-n
        else:
            n=n-m
    return m
    
def lcm1(m,n):
    return m*n//gcd1(m,n)

def gcd2(m,n):
    while n!=0:
        r=m%n
        m=n
        n=r
    return m

def lcm2(m,n):# Least common multiple
    return m*n//gcd2(m,n)

print reduce(lcm2,range(1,21))
print reduce(lcm1,range(1,21))

#Method II
N=20
def isprime(n):
    n = abs(int(n)) # make sure n is a positive integer
    if n < 2:       # 0 and 1 are not primes
        return False
    if n == 2:      # 2 is the only even prime number
        return True
    if not n & 1:   # all other even numbers are not primes
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

import math
p=2
ret=1
limit=math.sqrt(N)
while p<=N:
    if isprime(p):
        if p>limit:
            ret*=p
        else:
            m=int(math.floor(math.log(N)/math.log(p)))
            ret*=(p**m)
    p=p+1
print ret