
def process_list(file_name):
    grades = []
    female_grades = []
    male_grades = []
    # Read the file
    inputFile = open(file_name,'r')
    line = (inputFile.readline()).rstrip()
    while line != '':
        grade = int(line)
        grades.append(grade)
        line = (inputFile.readline()).rstrip()
        if line == "female":
            female_grades.append(grade) 
        elif line == "male":
            male_grades.append(grade) 
        line = (inputFile.readline()).rstrip()
    
    grade_average = round(sum(grades) / len(grades),2)
    female_grade_average = round(sum(female_grades) / len(female_grades),2)
    male_grade_average = round(sum(male_grades) / len(male_grades),2)

    # Print Average Values
    print("\nThe average math grade of all the students: " , grade_average)
    print("The average math grade of all female students: " , female_grade_average)
    print("The average math grade of all male students: " ,male_grade_average)
    
    import matplotlib.pyplot as plt
    
    # prepare list of two averages
    averages = [female_grade_average , male_grade_average]
    slice_labels = ['Females','Males']
    plt.pie(averages , labels=slice_labels, autopct='%1.2f%%')

def main():
    process_list("math.txt") 

main()
