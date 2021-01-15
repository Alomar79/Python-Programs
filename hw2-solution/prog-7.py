def calc_average(s1,s2,s3,s4,s5):
    average = (s1 + s2 + s3 + s4 + s5) / 5    
    return average

def determine_grade(sc):
    grade = False
    if sc >=90 and sc <= 100:
        grade = "A"
    elif sc >=80 and sc <= 89:
        grade = "B"
    elif sc >=70 and sc <= 79:
        grade = "C"
    elif sc >=60 and sc <= 69:
        grade = "D"
    elif sc >=0 and sc <= 59:
        grade = "F"
    return grade

def main():
    sc1 = int(input("Enter first score: "))
    sc2 = int(input("Enter second score: "))
    sc3 = int(input("Enter third score: "))
    sc4 = int(input("Enter forth score: "))
    sc5 = int(input("Enter fifth score: "))
    scoreList = [sc1, sc2, sc3, sc4, sc5]
    invalid_Score = False
    for sc in scoreList:
        if sc not in range(0, 101):
            invalid_Score = True
    if invalid_Score == True:
        print("Please!, Enter a valid score between 0 and 100")
    else:
        avg = calc_average(sc1,sc2,sc3,sc4,sc5)
        # print Grades Table:
        print ("\n  Score \t Grade")
        print("  =====================")
        for sc in scoreList:
            print("   ", sc , "\t\t  ", determine_grade(sc))
        print ("  Average \t" , avg)
        print()

main()
    

