# Write a complete Python program to find the largest of three numbers. 
# Numbers are entered by the user and expected to be either integers 
# or floats. Sample RUN (Use input in Bold)
# Enter first number: 3.4
# Enter first number: 89
# Enter first number: 4
# Largest is 89


x= float(input("Enter 1st  number : "))
y = float(input("Enter 2nd number : "))
z = float(input("Enter 3rd  number : "))
if (x >= y):
    if(x >= z):
        largest = x
    else:
        largest = z
elif(y >= z):
    largest = y
else:
    largest = z
print(" largest  is: ", largest)
