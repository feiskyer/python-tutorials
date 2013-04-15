#Project Euler Problem 9  
# Findthe only Pythagorean triplet, {a, b, c}, for which a + b + c = 1000  
# and get the product abc  
 
def abc1():
    print ([a*b*(1000-b-a) for a in range(1,501) for b in range(1,501) \
      if a**2+b**2==(1000-b-a)**2])  

def abc2(): # use xrange()
    print ( [a*b*(1000 - b -a) for b in xrange(1,500+1) for a in xrange(b,500+1) \
              if a * a + b * b == ((1000 -b -a) * (1000 - b - a))])  

if __name__=='__main__':
    import profile  # profile the program
    profile.run("abc1()")
    profile.run("abc2()")  