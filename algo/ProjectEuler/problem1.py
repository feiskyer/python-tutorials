# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The summ of these multiples is 23.
# Find the summ of all the multiples of 3 or 5 below 1000.

target=999

# method I
summ=0
for i in range(1,target+1): # range not include 1000
    if i%3==0 or i%5==0:
        summ+=i

print summ

# method II
def SumDivisibleBy(n):
    p=target/n
    return n*p*(p+1)/2

print SumDivisibleBy(3)+SumDivisibleBy(5)-SumDivisibleBy(15)