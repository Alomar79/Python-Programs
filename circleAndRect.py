x = input("Enter first letter of Geometric shape: ")

if x == 'c' or x == 'C':
    r = float(input('Enter the radius: '))
    circleArea = 3.14 * r * r
    circleCircumference = 2 * 3.14 * r
    print('Circle Area = ', format(circleArea, '.2f'))
    print('Circle Circumference = ', format(circleCircumference, '.2f'))
elif x == 'r' or x == 'R':
    b = float(input('Enter the base of Rect: '))
    h = float(input('Enter the height of Rect: '))
    rectArea = b * h
    rectPerimeter = 2 * (b + h)
    print('Rect Area = ', format(rectArea, '.2f'))
    print('Rect Perimeter = ', format(rectPerimeter, '.2f'))
else:
    print('Wrong input!')


