# write program that ask user for two numbers. 
# the program then calls a function that computes the area of the square with the first number 
# and the area of the circle with the second number and states which one is bigger.

def computeArea(num1, num2):
    squareArea = num1 * num1
    circleArea = 3.14 * num2 * num2
    if circleArea> squareArea:
        print('the circle of radius '+str(num2)+' is bigger than the sequare of size ' + str(num1))
    else:
        print('the sequare of size '+str(num1)+' is bigger than the circle of radius ' + str(num2))
    

first = float(input('Enter the first number: '))
second = float(input('Enter the second number: '))
computeArea(first, second)


input()
