
def allot_vaccine(average1,average2):
    if average1 > average2 and average1 > 50:
        print("the vaccine should be allotted to building 1 \n")
    elif average2 > average1 and average2 > 50:
        print("the vaccine should be allotted to building 2 \n")
def read_file(name_of_file):
    x = 0
    Total = 0    
    inputFile = open(name_of_file, "r")
    y = (inputFile.readline()).rstrip()
    while y != '':
        age = float(y)
        Total += age        
        y = (inputFile.readline()).rstrip()
        x =x + 1
    average = Total / x
    return average
def main():
    average1 = read_file("Building1.txt")
    average2 = read_file("Building2.txt")

    allot_vaccine(average1,average2)

main()

