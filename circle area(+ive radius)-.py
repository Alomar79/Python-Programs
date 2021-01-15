# Write a Python program which accepts the radius of a circle 
# from the user and compute the area. If the radius is 
# NOT a positive value exit with an error message. 
# PI should be declared as a constant. 
# (Format the output -> 2 decimal places)

r = float(input("Enter radius r :"))
PI = 3.14
if r > 0:
    	area = PI * r*r
    	print('area of circle = ', format(area, '.2f'))
else:
print('Error, radius must be positive number')
