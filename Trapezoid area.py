#Write a Python program that uses a function to find 
# the area of Trapezoid. 
# The function receives three values a, b, and h as shown in the figure. 
# The function returns the area to
# A = (a+b)h/2
the caller.

def computeArea(a, b, h):
    A = (a + b) * h / 2
    return A

# receive values.
upperSide = float(input('Enter the upper side:'))
bottomSide = float(input('Enter the bottom side:'))
height = float(input('Enter the height of Trapezoid:'))

# Call the function.
area = computeArea(upperSide, bottomSide, height)
print('The area of Trapezoid is : ', area)