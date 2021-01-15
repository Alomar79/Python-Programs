#  Write a while loop that asks the user to enter two numbers. 
# The numbers should be added and the sum displayed. 
# The user should be asked if he or she wishes to perform the 
# operation again. If so, the loop should repeat; 
# otherwise it should terminate.

inp = 'yes'
while (inp=='yes'):
    number1 = int(input("Enter value:"))
    number2 = int(input("Enter value:"))
    sum = number1 + number2
    print('sum of ',number1,'and ',number2,' equal : ', sum)
    inp = input("Do you want to perform the operation again? [yes]/[no]: ")
