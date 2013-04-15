#coding: UTF-8
# Find the sum of all the primes below two million.
import math

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

def mul1(n):
    s=0
    for i in xrange(0,n):
        if isprime(i):
            s+=i
    print s

#Sieve of Eratosthenes方法
#由于一个合数总是可以分解成若干个质数的乘积，那么如果把质数
#（最初只知道2是质数）的倍数都去掉，那么剩下的就是质数了。
#例如要查找100以内的质数，首先2是质数，把2的倍数去掉；此时3
#没有被去掉，可认为是质数，所以把3的倍数去掉；再到5，再到7，
#7之后呢，因为8，9，10刚才都被去掉了，而100以内的任意合数肯
#定都有一个因子小于10（100的开方），所以，去掉，2，3，5，7
#的倍数后剩下的都是质数了。

def getPrimeList(limit):
    sievebound = (limit-1) / 2
    sieve = [False] * (sievebound + 1)
    crosslimit = (int(math.sqrt(limit)) - 1) / 2
    for i in range(1, crosslimit+1):
        if not sieve[i]: # 2*i+1 is prime, mark multiples
            for j in range(2*i*(i+1), sievebound+1, 2*i+1):
                sieve[j] = True
    sieve = [2*i+1 for i in range(1, sievebound+1) if not sieve[i]]
    sieve.insert(0, 2)
    return sieve
def mul2(n):
    print sum(getPrimeList(n))
    
if __name__=='__main__':
    import profile  # profile the program
    profile.run("mul1(2000000)")    # 26.938s
    profile.run("mul2(2000000)")    # 0.469s