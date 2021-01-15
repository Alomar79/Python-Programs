# Using the following chart, write if/elif statements that 
# assigns .10, .15, or .20 to commission, depending on the 
# value in sales. Exit with an error message if the 
# sales value if less than zero
#         sales            comm
#       0 to 10000          10%
#       10000 to 15000      15%
#       over 15000          20%
Sales = int(input("Enter the value of sales : "))
if (Sales >= 0) and (Sales <= 10000):
    comm = 0.10
elif(Sales > 10000) and (Sales <= 15000):
    comm = 0.15
elif(Sales > 15000):
    comm = 0.20
else: 
    print('Wrong! the value must be positive')
print( 'commission rate = ', format(comm , '.2f'))
