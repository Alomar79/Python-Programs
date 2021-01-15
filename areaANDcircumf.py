x = input("Enter first letter of peometric shape: ")

if(x == "c" or x == "C"):
    circleArea = 0
    r = float(input('Enter the radius: ')
    circleArea = 3.14 * r * r
    circleCircumference = 2 * 3.14 * r
    print('Circle Area = ', circleArea)
    print('Circle Circumference = ', circleCircumference)
else if(x == 'r' or x == 'R'):
    b = float(input('Enter the base of Rect: ')
    h = float(input('Enter the height of Rect: ')
    rectArea = b * h
    rectPerimeter = 2 * (b + h)
    print('Rect Area = ', rectArea)
    print('Rect Perimeter = ', rectPerimeter)
    
