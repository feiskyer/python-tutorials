# Find the largest palindrome made from the product of two 3-digit numbers.

# Method I
def int_to_list(n):
    return map(int,str(n))

def is_palindrome(n):
    l=int_to_list(n)
    return l== list(reversed(l))

print  max([x*y for x in range(1000,100,-1)\
             for y in range(1000,100,-1)\
              if is_palindrome(x*y) ])

# Method II
print max(filter(lambda x: x == int(''.join(reversed(str(x)))),\
           [x * y for x in range(100, 1000) for y in range(100, 1000)]))