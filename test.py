fact = 1

def Factorial(N):
    fact = 1    
    if(N==0):
        fact = 1
    elif N>0:
        while N >=1:
            fact = fact * N
            N = N - 1     
    return fact

# main
number = int(input("Enter Number: "))

f = Factorial(number) + fact

print(f)










