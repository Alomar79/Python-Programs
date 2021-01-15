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
def main():
    number = int(input('Enter positive number:'))
    print('Factorial (', number, ') = ', Factorial(number))
    
main()
