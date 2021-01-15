# Write a Python program that uses a function to find and return 
# the factorial of a positiveinteger n.
# The function the receives a value and returns its factorial. 
# If the passed parameter is negative, 
# the function return the string “ERROR”. 
# Factorial of zero is one. Test your function.

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

number = int(input('Enter positive number:'))
print('Factorial (', number, ') = ', Factorial(number))

