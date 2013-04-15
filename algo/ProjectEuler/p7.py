# What is the 10001st prime number?

def isprime(n):
    n = abs(int(n))
    if n < 2:    
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def nth_prime(n):
    if n==1:
        return 2
    num=1
    i=3
    while i>1:
        if isprime(i):
            num=num+1
            if num==n:
                return i
        i+=2
        
print nth_prime(6)
print nth_prime(10001)