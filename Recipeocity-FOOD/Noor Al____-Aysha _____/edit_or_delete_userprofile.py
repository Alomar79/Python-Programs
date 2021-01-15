import os
import datetime
import create_or_load_userprofile

EDIT_NAME_CHOICE = 1
EDIT_DOB_CHOICE = 2
EDIT_GENDER_CHOICE = 3
EDIT_HEIGHT_CHOICE = 4
EDIT_WEIGHT_CHOICE = 5
EDIT_ACTIVITY_CHOICE = 6
EDIT_ALLERGIES_CHOICE = 7

def edit_date():
    
    x = datetime.datetime.now()
    thisDay = x.strftime("%d")
    thisMonth = x.strftime("%m")
    thisYear = x.strftime("%Y")
    thisHour = x.strftime("%H")
    thisMinute = x.strftime("%M")
    thisSecond = x.strftime("%S")
    Editdate = thisDay+'/'+thisMonth+'/'+thisYear+','+thisHour+':'+thisMinute+':'+thisSecond
    return Editdate

def change_user_information(old_value , new_value, username):
    # found = False
    new_record = ""
    inputfile = open('userInformation.txt','r')
    outfile = open('temp.txt','w')
    # copy header names
    outfile.write(inputfile.readline().rstrip())
    line = inputfile.readline().rstrip()
    while line != '':        
        record_list = line.rstrip().split()
        if username in record_list:
            # found = True
            for x in record_list:
                record_list[13] = edit_date()
                if x==old_value:
                    x = new_value
                if new_record != '':
                    new_record += '\t'                
                new_record += str(x)
            
            outfile.write( '\n' + new_record)
            line = inputfile.readline().rstrip()
        else:
            outfile.write('\n' + line )
            line = inputfile.readline().rstrip()    
    outfile.close()
    inputfile.close()
    outfile.close()
    inputfile.close()    
    os.remove('userInformation.txt')
    os.rename('temp.txt' , 'userInformation.txt')
    return new_value

def read_information(username):
    record_list = []
    inputfile = open('userInformation.txt','r')
    next(inputfile)    
    records = inputfile.readlines() 
    found = False
    while found ==False:
        for x in records:        
            record_list = x.rstrip('\n').split()
            if username in record_list:
                found = True
                return record_list
    return record_list       
    
def activityValue_calculate(activity):
    Activity = int(activity)
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
    return activity_value

def display_activity_menu():
    print('Which one of the following statements describes your activity level?')
    print("\n1) Little/No exercise")
    print("2) Light exercise")
    print("3) Moderate exercise (3-5 days/week)")
    print("4) Very active (6-7 days/week)")
    print("5) Extra active (very active & physical job)\n")

def BMR_calculate(gender , Weight, Height , Age):
    if gender =='female':
        BMR = 655.1 +(9.563* float(Weight)) +(1.85* float(Height)*100)-(4.676 * float(Age))
    else:
        BMR = 66.47 +(13.75* float(Weight)) +(5.003* float(Height)*100)-(6.755 * float(Age))
    BMR = float(format(BMR , '.2f'))
    return BMR

def BMI_range_calculate(BMI):
    bmi = float(BMI)
    if bmi < 18.5:
        BMIRange = 'Underweight'
    elif bmi>= 18.5 and BMI <=24.9:
        BMIRange = 'Normal'
    elif bmi>= 25.0 and BMI <=29.9:
        BMIRange = 'Overweight'
    elif bmi>= 30.0:
        BMIRange = 'Obese'
    return BMIRange

def read_allergies():
    # read ingredients using create_or_load_userprofile module
    ingredients , ingredient_names, ingredient_numbers = create_or_load_userprofile.read_ingredients('ingredients.csv')
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
    return Allergies
    
def edit_profile(filename , username):
    choice = 0
    print('These are the fields that you can edit in your profile:')    
    print('1) Name')
    print('2) Date of Birth (dd/mm/yyyy')
    print('3) Gender')
    print('4) Height (m)')
    print('5) Weight (Kg)')
    print('6) Activity level')
    print('7) Food allergies')
    choice = int(input('Enter a number to select a field to edit:'))
    if choice == EDIT_NAME_CHOICE:
        new_name = str(input('Enter your new name:'))
        username = change_user_information(username , new_name, username)
    if choice == EDIT_DOB_CHOICE:
        DOB = str(input('Enter your birth date as follows(dd/mm/yyyy) : '))
        record = read_information(username)
        birthDate = DOB.split('/')
        x = datetime.datetime.now()
        thisYear = x.strftime("%Y")
        year_of_birth = int(birthDate[2])
        Age = int(thisYear) - year_of_birth
        BMI = float(format(float(record[3]) / (float(record[2])**2) , '.2f'))
        BMR = BMR_calculate(record[6] , record[3], record[2] , Age)
        activity_value = activityValue_calculate(record[10])
        TEE = format(BMR * activity_value , '.2f')
        change_user_information(record[4] , DOB ,username)
        change_user_information(record[5] , Age ,username)
        change_user_information(record[9] , BMR ,username)
        change_user_information(record[11] , TEE ,username)
    if choice == EDIT_GENDER_CHOICE:
        new_gender = (str(input('Enter your gender(male / female) : '))).lower()
        record = read_information(username)
        BMR = BMR_calculate(new_gender , record[3], record[2] , record[5])
        activity_value = activityValue_calculate(int(record[10]))
        TEE = format(BMR * activity_value , '.2f')
        change_user_information(record[6] , new_gender ,username)
        change_user_information(record[9] , BMR ,username)
        change_user_information(record[11] , TEE ,username)
    if choice == EDIT_HEIGHT_CHOICE:
        new_height = float(input('Enter your height(in metres) : '))
        record = read_information(username)
        BMI = float(format(float(record[3]) / (new_height**2) , '.2f'))
        BMIrange = BMI_range_calculate(BMI)
        BMR = BMR_calculate(record[6] , record[3], new_height , record[5])
        activity_value = activityValue_calculate(int(record[10]))
        TEE = format(BMR * activity_value , '.2f')
        change_user_information(record[2] , new_height ,username)
        change_user_information(record[7] , BMI ,username)
        change_user_information(record[8] , BMIrange ,username)
        change_user_information(record[9] , BMR ,username)
        change_user_information(record[11] , TEE ,username)
    if choice == EDIT_WEIGHT_CHOICE:
        new_weight = float(input('Enter your weight(in kilogram) : '))
        record = read_information(username)
        BMI = float(format(new_weight / (float(record[2])**2) , '.2f'))
        BMIrange = BMI_range_calculate(BMI)
        BMR = BMR_calculate(record[6] , new_weight, record[2] , record[5])
        activity_value = activityValue_calculate(int(record[10]))
        TEE = format(BMR * activity_value , '.2f')
        change_user_information(record[3] , new_weight ,username)
        change_user_information(record[7] , BMI ,username)
        change_user_information(record[8] , BMIrange ,username)
        change_user_information(record[9] , BMR ,username)
        change_user_information(record[11] , TEE ,username)
    if choice == EDIT_ACTIVITY_CHOICE:
        display_activity_menu()
        new_activity = int(input('Enter your activity number: '))
        record = read_information(username)
        activity_value = activityValue_calculate(new_activity)
        BMR = BMR_calculate(record[6] , record[3], record[2] , record[5])
        TEE = format(BMR * activity_value , '.2f')
        change_user_information(record[10] , new_activity ,username)
        change_user_information(record[11] , TEE ,username)
    if choice == EDIT_ALLERGIES_CHOICE:
        allergies = read_allergies()
        record = read_information(username)
        change_user_information(record[12] , allergies ,username)
        
    print("\nUser Information changed successfully! \n")
    return username
 
def delete_profile(username):
    inputfile = open('userInformation.txt','r')
    outfile = open('temp.txt','w')
    
    # copy header names
    outfile.write(inputfile.readline())
    line = (inputfile.readline()).rstrip()
    # copy userInformation.txt records to temp.txt
    
    counter = 0
    while line != '':
        record_list = line.rstrip('\n').split()
        if username not in record_list:
            outfile.write(line + '\n')
            counter += 1
        line = (inputfile.readline()).rstrip()
    
    outfile.close()
    inputfile.close()
    outfile.close()
    inputfile.close()
    
    os.remove('userInformation.txt')
    #os.close()
    if counter != 0:
        os.rename('temp.txt' , 'userInformation.txt')
    else:
        os.remove('temp.txt')
    print('the record deleted successfully')
    username = 'stranger'
    return username
           

def edit_or_delete_profile(username):
    found = False
    while found == False:        
        print('\nHello', username)
        print('you can perform one of the following operations:')
        print('1) Delete your profile')
        print('2) Edit your user profile\n')
        answer = int(input('Which action would you like to perform?'))
        if answer == 1:
            inputfile = open('userInformation.txt','r')
            next(inputfile)    
            records = inputfile.readlines()             
            inputfile.close()            
            for x in records:        
                record_list = x.rstrip('\n').split()
                if username in record_list: 
                    found = True
                    username = delete_profile(username)                 
            if found == False:
                print('No profile under name of', username)
                username = str(input('Please enter your name to load your profile: '))
       
        elif answer == 2:
            print('Hello', username)
            inputfile = open('userInformation.txt','r')
            next(inputfile)
            records = inputfile.readlines()             
            inputfile.close()            
            for x in records:        
                record_list = x.rstrip('\n').split()
                if username in record_list: 
                    found = True
                    username = edit_profile('userInformation.txt', username)                 
            if found == False:
                print('No profile under name of', username)
                username = str(input('Please enter your name to Edit your profile: '))
        
    return username