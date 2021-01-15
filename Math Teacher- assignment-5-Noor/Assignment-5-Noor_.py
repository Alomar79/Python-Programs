
def average(list): 
    return round( sum(list) / len(list) , 2)

def process_list(file_name):
    import matplotlib.pyplot as plt
    
    grades = []
    femaleGrades = []
    maleGrades = []
    # Reading the file
    inFile = open(file_name,'r')
    line = inFile.readline()
    line = line.strip("\n")
    while line != '':
        grade = int(line)
        grades.append(grade)
        line = inFile.readline()
        line = line.strip("\n")
        if line == "female":
            femaleGrades.append(grade) 
        elif line == "male":
            maleGrades.append(grade) 
        line = inFile.readline()
        line = line.strip("\n")
    
    # Calculate Statistics
    gradeAverage = average(grades)
    female_gradeAverage = average(femaleGrades)
    male_gradeAverage = average(maleGrades)

    # Print Average Values
    print("The average math grade of all the students: " , gradeAverage)
    print("The average math grade of all female students: " , female_gradeAverage)
    print("The average math grade of all male students: " ,male_gradeAverage)
    print("\n\n\n")
   
    # Plotting
    # list of two averages
    average_values = [female_gradeAverage , male_gradeAverage]
    slice_labels = ['Females','Males']
    plt.title("Average Performance of female and male Students in Math")
    plt.pie(average_values , labels=slice_labels, autopct='%1.2f%%')
    plt.show()

# Main Function
def main():
    process_list("math.txt") 

main()
