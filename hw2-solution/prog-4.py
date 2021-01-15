def maximum(a, b, c):
    if a >= b:
        if(a >= c):
            max = a
        else:
            max = c
    elif b > a:
        if(b >= c):
            max = b
        else:
            max = c

    return max

def main():
    num1 = float(input('Enter 1st number:'))
    num2 = float(input('Enter 2nd number:'))
    num3 = float(input('Enter 3rd number:'))
    print('the maximum is: ', maximum(num1, num2, num3) )

main()
