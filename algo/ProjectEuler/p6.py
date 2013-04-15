# Find the difference between the sum of the squares of the first 
# one hundred natural numbers and the square of the sum.

def diff(n):
    square_of_sum=(n*(n+1)/2)**2
    sum_of_square=n*(n+1)*(2*n+1)/6
    return square_of_sum-sum_of_square

print diff(10)
print diff(100)