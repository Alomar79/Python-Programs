# In a new program, use the function you wrote in question 2 
# to print the factorials of values from 1 to 10. Use for loop.

def Factorial(n):
    fact = 1    
    if n < 0:
        fact = 'Error'
    elif n == 0:
        fact = 1
    else:
        x = n
        while x > 0:
            fact = fact * x
            x -=1
    return fact

for x in range(1 , 11):
    print('Factorial (', x ,') = ', Factorial(x))