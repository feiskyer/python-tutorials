# By considering the terms in the Fibonacci sequence 
# whose values do not exceed four million, find the 
# summ of the even-valued terms.

# Method I
summ=0
a=1
b=1
while b<4000000:
    if b%2==0:
        summ+=b
    s=a+b
    a=b
    b=s
print summ

# Method II
# 1 1 2 3 5 8 13 21 34 55 89 144
summ=0
a=1
b=1
while a<4000000:
    summ+=a+b
    temp=a+b+b
    b=temp+a+b
    a=temp
print summ