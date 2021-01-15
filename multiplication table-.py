# Write a python program that asks the user to enter an integer N, 
# and it then prints the multiplication table (up to 10) for that integer.

N = int(input("Enter integer number: "))

print("\nMultiplication Table : \n")
for x in range(1,11):
    print(N,"*",x,"=",N*x)