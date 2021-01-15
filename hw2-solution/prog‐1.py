def computeArea(a, b, h):
    A = (1/2)*(a+b)*h
    return A

def main():
    # receive values.
    upperSide = float(input('Enter the upper side:'))
    bottomSide = float(input('Enter the bottom side:'))
    height = float(input('Enter the height of Trapezoid:'))

    # Call the function.
    area = computeArea(upperSide, bottomSide, height)
    print('The area of Trapezoid is : ', area)
    
main()