
pwd = int(input("Enter the password : "))
count = 1
while pwd!=128:
    if(count <5):
        print("wrong!, tray again")
        count = count + 1
        pwd = int(input("Enter the password : "))
    else:
        print("You exceeded the number of allowed attempts! ")
        break
if pwd ==128:
    print("True password")

