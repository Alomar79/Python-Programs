# In another program, use the function you wrote in question 5 
# to print the prime numbers between 1 and 100 using for loop.

def is_prime(n):
    if n==2:
        Prime = True
    elif n > 2:
        for i in range(2,n):
            if (n % i) == 0:
                Prime = False
                break
            else:
                Prime = True    
    else:
        Prime = False

    return Prime

for x in range(1, 101):
    if is_prime(x):
        print(x)
