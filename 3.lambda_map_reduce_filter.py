from functools import reduce

# Lambda

mx = lambda x:x*2
print(mx(5))

mx = lambda x,y:x+y
print(mx(5,5))

# Maps
n = [1,2,3,4]
print(list(map(lambda x:x**2, n)))

# Filter
n = [1,2,3,4]
print(list(filter(lambda x:x if x > 1 else None, n)))

# Reduce
n = [1,2,3,4]
print(reduce(lambda x,y:x*y, n))

# Reduce Fibanacci

fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
print(fib(5))

  
def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==0:
        return 0
    # Second Fibonacci number is 1 
    elif n==1: 
        return 1
    else: 
        print(Fibonacci(n-1)+Fibonacci(n-2)) 
        return Fibonacci(n-1)+Fibonacci(n-2) 
  
# Driver Program 
  
print(Fibonacci(5)) 

# Program to display the Fibonacci sequence up to n-th term where n is provided by the user

# change this value for a different result
nterms = 10

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(n1,end=' , ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1