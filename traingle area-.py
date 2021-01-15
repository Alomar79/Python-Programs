#	Write a Python program that will accept the base and height of a 
# triangle and compute the area. 
# (Format the output -> 2 decimal places)

base = float(input("Enter the base of triangle: "))
height = float(input("Enter the height of triangle: "))
area = (base * height)/2
print("the Area is: ", format(area, '.2f'))
