def main():
    sum = 0
    count = 1
    out = False    
    number = int(input('Please enter the number:'))
    
    while out == False and count <= 3:
        strNum = str(number)
        for x in strNum:
            x = int(x)
            sum += x        
        if sum == 15:
            out = True
            print('Hurray you won!!!')
        elif count<3 and sum != 15:
            print('Try again…')
            sum = 0
            count +=1
            out = False
            number = int(input('Please enter the number:'))
        else:
            print('Bye Bye')
            out = True            

main()