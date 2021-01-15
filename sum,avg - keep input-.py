# Write a Python program that keeps accepting positive numbers 
# from the user. The program quits the loop if the entered value 
# is negative. 
# The program prints the sum and the average of the accepted values.
# Sample RUN (Use input in Bold)
# Enter a number (-ve to quit): 10
# Enter a number (-ve to quit): 7.7
# Enter a number (-ve to quit): 3.4
# Enter a number (-ve to quit): 31.3
# Enter a number (-ve to quit): -1
# SUM = 52.4
# Average = 13.1
# (Format the output -> 3 decimal places)

sum = 0
j = 0
number = 0
while (number >= 0):
    number = float(input("Enter a number (-ve to quit): "))
    if number >= 0:
        sum = sum + number
        j = j + 1
average = sum / j
print('SUM = ', format(sum, '.3f'))
print('Average = ', format(average, '.3f'))
