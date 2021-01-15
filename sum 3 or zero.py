# Write a Python program that will accept three integers to 
# find their sum. However, if any two values are equal sum will be zero.

x = int(input('Enter the 1st number: '))
y = int(input('Enter the 2nd number: '))
z = int(input('Enter the 3rd number: '))
if (x == y) or (x == z) or (num2 == z):
    sum = 0
else:
    sum = x + y + z
print('Sum = ' , sum)
