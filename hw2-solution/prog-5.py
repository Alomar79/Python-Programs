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

def main():
    number = int(input('Enter integer number:'))
    if is_prime(number):
        print('\nthe number (',number, ') is prime \n' )
    else:
        print('the number (',number, ') is NOT prime \n' )

main()

