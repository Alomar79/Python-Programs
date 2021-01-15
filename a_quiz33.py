
def calculate_average(a , b , c):
    avg = format((a + b + c) / 3 , ".2f")
    return avg
    
for i in range(1,11):
    name = str(input("Enter your name: "))
    grade1 = int(input("Enter grade1 : "))
    grade2 = int(input("Enter grade2 : "))
    grade3 = int(input("Enter grade3 : "))
    average = calculate_average(grade1 , grade2 , grade3)
    out = open("studentsGrades.txt", "a")
    str1 = name + "\t" + str(grade1) +"\t"+ str(grade2)  +"\t"+ str(grade3)  +"\t"+ str(average) + "\n"
    out.write( str1 )
    out.close()


    

