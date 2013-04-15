# Project Euler Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
 

import math

# My method
def prime(n):
    i=2
    while i<n/2:
        if n%i==0:
            return False
        i+=1
    return True

def max_factor(n):
    i=2
    fact=1
    while i<=n:
        if (n%i==0) and prime(i):
            fact=i
            n=n/i
            while n%i==0:
                n=n/i
        i+=1
    return fact

print max_factor(600851475143)

# Optimized method
# 2 is the only even prime, increase factor with 2 every step
#every number n can at most have one prime factor greater than sqrt(n)

def max_factor_opt(n):
    if n%2==0:
        fact=2
        n=n/fact
        while n%2==0:
            n=n/2
    else:
        fact=1
    i=3
    maxFactor=math.sqrt(n)
    while n>1 and i<=maxFactor:
        if n%i==0:
            fact=i
            n=n/i
            while n%fact==0:
                n=n/fact
            maxFactor=math.sqrt(n)
        i+=2
    if n==1:
        return fact
    else:
        return n

print max_factor_opt(600851475143)