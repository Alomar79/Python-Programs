import os
def writeToFile(fileName, header_string , user_information ):
   
    # Display header names
    if not os.path.exists(fileName):
        out = open(fileName, "w")
        out.write(header_string)
    # open file to append new person    
    out = open(fileName, "a")
    out.write(user_information + '\n')
    out.close()
   
def read_ingredients(CSV_FILENAME):
    infile = open(CSV_FILENAME,'r')
    next(infile)
    ingredients_list = []
    ingredient_names_list = []
    ingredient_numbers_list = []
    all_lines = infile.readlines()    
    for x in all_lines:        
        line_list = x.strip().split(';')
        ingredients_list.append(str(line_list[1]) +'\t\t'+ str(line_list[0]))
        ingredient_names_list.append(line_list[0])
        ingredient_numbers_list.append(int(line_list[1]))
    infile.close()
    return ingredients_list , ingredient_names_list , ingredient_numbers_list
    
def create_profile():        
    import datetime
    
    x = datetime.datetime.now()
    thisDay = x.strftime("%d")
    thisMonth = x.strftime("%m")
    thisYear = x.strftime("%Y")
    thisHour = x.strftime("%H")
    thisMinute = x.strftime("%M")
    thisSecond = x.strftime("%S")
    Joindate = thisDay+'/'+thisMonth+'/'+thisYear+','+thisHour+':'+thisMinute+':'+thisSecond
    Name = str(input('Enter your name please:'))
    DOB = str(input('Enter your birth date as follows(dd/mm/yyyy) : '))
    Height = float(input('Enter your height(in meters) :'))
    Weight = float(input('Enter your weight(in kilograms) :'))
    Gender = (str(input('Enter your gender pleas( male / female) :'))).lower()
    
    birth_list = DOB.split('/')
    year_of_birth = int(birth_list[2])
    Age = int(thisYear) - year_of_birth
    BMI = float(format(Weight / (Height**2) , '.2f'))
    if BMI < 18.5:
        BMIRange = 'Underweight'
    elif BMI>= 18.5 and BMI <=24.9:
        BMIRange = 'Normal'
    elif BMI>= 25.0 and BMI <=29.9:
        BMIRange = 'Overweight'
    elif BMI>= 30.0:
        BMIRange = 'Obese'
    # calculate the Basal Metabolic Rate (BMR)
    if Gender =='female':
        BMR = 655.1 +(9.563* Weight) +(1.85* Height*100)-(4.676 * Age)
    else:
        BMR = 66.47 +(13.75* Weight) +(5.003* Height*100)-(6.755 * Age)
    BMR = float(format(BMR , '.2f'))
    print('Which one of the following statements describes your activity level?')
    print("\n1) Little/No exercise")
    print("2) Light exercise")
    print("3) Moderate exercise (3-5 days/week)")
    print("4) Very active (6-7 days/week)")
    print("5) Extra active (very active & physical job)\n")
    Activity = int(input("Please Enter number that describes your activity level from the list above: "))
    while Activity not in range(1,6):
        Activity = int(input("Please Enter number that describes your activity level from the list above: "))
    if Activity == 1:
        activity_value = 1.2
    elif Activity == 2:
        activity_value = 1.375
    elif Activity == 3:
        activity_value = 1.55
    elif Activity == 4:
        activity_value = 1.725
    elif Activity == 5:
        activity_value = 1.9
    TEE = format(BMR * activity_value , '.2f')
    
    # call function to display ingredients
    ingredients , ingredient_names, ingredient_numbers = read_ingredients('ingredients.csv')
    print('\n\t Ingredient List')
    print('\n\t ===============')
    print("\nIngredient number \t Ingredient name\n")
    for x in ingredients:
        print(x)
    Allergies = ''   # string variable to store allergies 
    ingredient_number = int(input('Enter ingredient number that you are allergic to: '))
    while ingredient_number != -1:
        if ingredient_number in ingredient_numbers:
            index = ingredient_numbers.index(ingredient_number)
            if Allergies !='':
                Allergies += ','
            Allergies += ingredient_names[index]
        else:
            print('\nWrong input!, select again\n')
        ingredient_number = int(input('Enter ingredient number that you are allergic to: '))
    if Allergies =='':
        Allergies = '-'
    
    header_string = "Join Date \t\t Name \t Height \t Weight \t birthDate \t Age" \
        +"\tGender \t BMI\tBMI range\tBMR\tActivity\tTEE\tAllergies\tEdit Date \n"
    
    EditDate = '-'
    user_information = Joindate+'\t'+Name+'\t'+str(Height)+'\t'+str(Weight)+'\t'\
        + DOB +'\t'+ str(Age) +'\t'+ Gender +'\t'+ str(BMI) +'\t'+ BMIRange +'\t'+ str(BMR) +'\t'\
        + str(Activity) +'\t'+ str(TEE) +'\t'+ Allergies +'\t'+ EditDate
    
    # call function to write information to the file
    writeToFile('userInformation.txt' , header_string , user_information)
    print('\nProfile for user',Name,'is crated and loaded successfully.\n')
    return Name

def return_activity(activity_number):
    activity = int(activity_number)
    if activity == 1:
        activity_level = "Little/No exercise"
    elif activity == 2:
        activity_level = "Light exercise"
    elif activity == 3:
        activity_level = "Moderate exercise (3-5 days/week)"
    elif activity ==4:
        activity_level = "Very active (6-7 days/week)"
    elif activity == 5:
        activity_level = "Extra active (very active & physical job)"
    else:
        activity_level = "-"
    return activity_level

def load_profile(fileName , username):
    inputfile = open(fileName,'r')
    next(inputfile)    
    records = inputfile.readlines() 
    found = False
    while found ==False:
        for x in records:        
            record_list = x.rstrip('\n').split()
            if username in record_list:
                found = True
        if found == False:
            print('There is no profile under the name', username)
            username = str(input("Please enter your name to load your profile: "))   
    
    for x in records:        
        record_list = x.rstrip('\n').split()
        if username in record_list:
            print('+-----------------------+')
            print('|+---------------------+|')
            print('|| {0:20}||'.format(username + '\'s Profile'))
            print('|+---------------------+|')
            print('+-----------------------+')
            print('\nJoin Date            : ',record_list[0])                
            print('Date of Birth        : ',record_list[4])
            print('Age                  : ',record_list[5])
            print('Gender               : ',record_list[6])
            print('Height (m)           : ',record_list[2])
            print('Weight (kg)          : ',record_list[3])
            print('Body Mass Index (BMI)        : ',record_list[7])
            print('BMI Range                    : ',record_list[8])
            print('Basal Metabolic Rate (BMR)   : ',record_list[9])
            print('Activity level               : ',return_activity(record_list[10]))
            print('Total Energy Expenditure(TEE): ',record_list[11])
            print('Food Allergies               : ',record_list[12])
            found = True
            break
    inputfile.close()
    return username   
    
    
def create_or_load_profile(username):
    # username = ''
    if os.path.exists('userInformation.txt'):
        answer = (str(input("Do you create profile before? (Y/N): "))).lower()
        while answer !='y' and answer !='n':
            answer = (str(input("Do you create profile before? (Y/N): "))).lower()
        if answer=='y':            
            username = load_profile('userInformation.txt', username)
            return username
        elif answer=='n':
            print('please create a new profile\n')
            username = create_profile()
            answer2 = (str(input('Do you want to view your profile information?(Y/N)'))).lower()
            if answer2 == 'y':
                load_profile('userInformation.txt', username)
            return username
    else:
        username = create_profile()
        return username
    
