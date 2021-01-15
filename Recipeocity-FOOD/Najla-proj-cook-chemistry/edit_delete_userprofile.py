import os
import create_load_profile
import datetime
# Constants for choices
EDIT_NAME = 1
EDIT_BIRTH_YEAR = 2
EDIT_GENDER = 3
EDIT_HEIGHT = 4
EDIT_WEIGHT = 5
EDIT_ACTIVITY = 6
EDIT_ALLERGIES = 7

# calculate  activity Value depend on activity number
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

# Prepare BMI Range depend on BMI value
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

# Calculate BMR depend on many arguments
def BMR_Calc(gender , Weight, Height , Age):
    if gender =='female':
        BMR = 655.1 +(9.563* float(Weight)) +(1.85* float(Height)*100)-(4.676 * float(Age))
    else:
        BMR = 66.47 +(13.75* float(Weight)) +(5.003* float(Height)*100)-(6.755 * float(Age))
    BMR = float(format(BMR , '.2f'))
    return BMR

#prepare editing date
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

# Edit user information (multi use)
def change_user_information(old_val , new_val, username):
    # found = False
    new_line_list = ""
    inputfile = open('userInformation.txt','r')
    # create new temporary file to transfer all lines except user line to it
    outfile = open('temp.txt','w')
    # copy header names
    outfile.write(inputfile.readline().rstrip())
    line = inputfile.readline().rstrip()
    # search about the username
    while line != '':        
        user_line = line.rstrip().rsplit()
        # if user is found, catch his line_list to change
        if username in user_line:
            for x in user_line:
                # add edit-date to the user line 
                user_line[13] = edit_date()
                # for each item in the line, check if equal to what to change
                # if true, change it with new value
                if x == old_val:
                    x = new_val
                if new_line_list != '':
                    new_line_list += '\t'                
                new_line_list += str(x)
            # write the line ( with new value) to the temporary file
            outfile.write( '\n' + new_line_list)
            line = inputfile.readline().rstrip()
        else:
            # for other lines, write them without change
            outfile.write('\n' + line )
            line = inputfile.readline().rstrip()    
    outfile.close()
    inputfile.close()
    outfile.close()
    inputfile.close()
    # remove old file  
    os.remove('userInformation.txt')
    # change name of temporary file to 'userInformation.txt'
    os.rename('temp.txt' , 'userInformation.txt')
    return new_val

# read user information from the file
def read_user_information(username):
    user_line = []
    inputfile = open('userInformation.txt','r')
    next(inputfile)    
    line_lists = inputfile.readlines() 
    found = False
    # Search about username
    while found ==False:
        for x in line_lists:        
            user_line = x.rstrip('\n').split()
            if username in user_line:
                found = True
                return user_line
    return user_line       

#print activity menu to the user
def display_activity_menu():
    print('Which one of the following statements describes your activity level?')
    print("\n1) Little/No exercise")
    print("2) Light exercise")
    print("3) Moderate exercise (3-5 days/week)")
    print("4) Very active (6-7 days/week)")
    print("5) Extra active (very active & physical job)\n")

# Read Allergies from the file 'userInformation.txt'
def read_new_allergies():
    # read ingredients using create_load_profile module
    ingredients , ingredient_names, ingredient_nums = create_load_profile.read_ingredients_from_file('ingredients.csv')
    print('\n\t Ingredient List')
    print('\n\t +++++++++++++++')
    print("\nIngredient number \t Ingredient name\n")
    for x in ingredients:
        print(x)
    Allergies = ''   # to store allergies 
    # Read ingredient number that the user allergic to
    ingredient_no = int(input('Enter ingredient# that allergic to(-1 to finish): '))
    while ingredient_no != -1:
        if ingredient_no in ingredient_nums:
            index = ingredient_nums.index(ingredient_no)
            if Allergies !='':
                Allergies += ','
            Allergies += ingredient_names[index]
        else:
            print('\nWrong !, select again\n')
        ingredient_no = int(input('Enter ingredient# that allergic to(-1 to finish): '))
    if Allergies =='':
        Allergies = '-'
    return Allergies

# display Edit Menu
def print_edit_menu():
    print('These are the fields that you can edit in your profile:')    
    print('1) Name')
    print('2) Date of Birth (dd/mm/yyyy')
    print('3) Gender')
    print('4) Height (m)')
    print('5) Weight (Kg)')
    print('6) Activity level')
    print('7) Food allergies')

# Edit profile Function
def edit_profile(filename , username):
    choice = 0
    # Print Edit Menu
    print_edit_menu() 
    # Ask to Enter the choice   
    choice = int(input('Enter a number to select a field to edit:'))
    # Read user information and return line as list
    line_list = read_user_information(username)
    if choice == EDIT_NAME:
        new_name = str(input('Enter your new name:'))
        # change the information by the function :
        # change_user_information(oldVal , newVal, username)
        username = change_user_information(username , new_name, username)
    # Edit Year and other relatives
    if choice == EDIT_BIRTH_YEAR:
        birth_year = str(input('Enter your birth year as follows(yyyy) : '))        
        #birthDate = birth_year.split('/')
        x = datetime.datetime.now()
        thisYear = x.strftime("%Y")
        #year_of_birth = int(birthDate[2])
        Age = int(thisYear) - int(birth_year)
        BMI = float(format(float(line_list[3]) / (float(line_list[2])**2) , '.2f'))
        BMR = BMR_Calc(line_list[6] , line_list[3], line_list[2] , Age)
        activity_value = activityValue_calculate(line_list[10])
        TEE = format(BMR * activity_value , '.2f')
        # call function to change the values
        change_user_information(line_list[4] , birth_year ,username)
        change_user_information(line_list[5] , Age ,username)
        change_user_information(line_list[9] , BMR ,username)
        change_user_information(line_list[11] , TEE ,username)
    # Edit gender and other relatives
    if choice == EDIT_GENDER:
        new_gender = (str(input('Enter your gender(male / female) : '))).lower()
        BMR = BMR_Calc(new_gender , line_list[3], line_list[2] , line_list[5])
        activity_value = activityValue_calculate(int(line_list[10]))
        TEE = format(BMR * activity_value , '.2f')
        # call function to change the values
        change_user_information(line_list[6] , new_gender ,username)
        change_user_information(line_list[9] , BMR ,username)
        change_user_information(line_list[11] , TEE ,username)
    # Edit height and other relatives   
    if choice == EDIT_HEIGHT:
        new_height = float(input('Enter your height(in metres) : '))
        BMI = float(format(float(line_list[3]) / (new_height**2) , '.2f'))
        BMIrange = BMI_range_calculate(BMI)
        BMR = BMR_Calc(line_list[6] , line_list[3], new_height , line_list[5])
        activity_value = activityValue_calculate(int(line_list[10]))
        TEE = format(BMR * activity_value , '.2f')
        # call function to change the values
        change_user_information(line_list[2] , new_height ,username)
        change_user_information(line_list[7] , BMI ,username)
        change_user_information(line_list[8] , BMIrange ,username)
        change_user_information(line_list[9] , BMR ,username)
        change_user_information(line_list[11] , TEE ,username)
    # Edit weight and other relatives
    if choice == EDIT_WEIGHT:
        new_weight = float(input('Enter your weight( in Kg ) : '))
        BMI = float(format(new_weight / (float(line_list[2])**2) , '.2f'))
        BMIrange = BMI_range_calculate(BMI)
        BMR = BMR_Calc(line_list[6] , new_weight, line_list[2] , line_list[5])
        activity_value = activityValue_calculate(int(line_list[10]))
        TEE = format(BMR * activity_value , '.2f')
        # call function to change the values
        change_user_information(line_list[3] , new_weight ,username)
        change_user_information(line_list[7] , BMI ,username)
        change_user_information(line_list[8] , BMIrange ,username)
        change_user_information(line_list[9] , BMR ,username)
        change_user_information(line_list[11] , TEE ,username)
    # Edit activity and other relatives
    if choice == EDIT_ACTIVITY:
        display_activity_menu()
        new_activity = int(input('Enter your activity number: '))
        activity_value = activityValue_calculate(new_activity)
        BMR = BMR_Calc(line_list[6] , line_list[3], line_list[2] , line_list[5])
        TEE = format(BMR * activity_value , '.2f')
        # call function to change the values
        change_user_information(line_list[10] , new_activity ,username)
        change_user_information(line_list[11] , TEE ,username)
    # Edit allergies
    if choice == EDIT_ALLERGIES:
        allergies = read_new_allergies()
        # call function to change the allergies
        change_user_information(line_list[12] , allergies ,username)
        
    print("\nUser Information changed successfully! \n")
    return username

# Delete user profile 
def delete_profile(username):
    inputfile = open('userInformation.txt','r')
    # create temporary file and transfer lines to it except that one need to delete
    outfile = open('temp.txt','w')    
    # copy header names
    outfile.write(inputfile.readline())
    line = (inputfile.readline()).rstrip()
    # copy userInformation.txt lines to temp.txt    
    counter = 0
    while line != '':
        user_line = line.rstrip('\n').split()
        # search about the username
        if username not in user_line:
            outfile.write(line + '\n')
            counter += 1
        line = (inputfile.readline()).rstrip()
    
    outfile.close()
    inputfile.close()
    outfile.close()
    inputfile.close()
    
    os.remove('userInformation.txt')
    # if more one line in the file
    if counter != 0:
        os.rename('temp.txt' , 'userInformation.txt')
    else:
        os.remove('temp.txt') # if the file empty, then delete it
    print('the profile deleted successfully')
    # after delete current username, we must remove it from the program
    username = 'stranger'
    return username

# control function in this module
# which call other functions to delete or load profile
def edit_delete_profile(username):
    catched = False
    while catched == False:        
        print('\nHello', username)
        print('you can perform one of the following operations:')
        print('1) Delete your profile')
        print('2) Edit your user profile\n')
        # ask to choose one task
        answer = int(input('Which action would you like to perform?'))
        if answer == 1: # Delete option
            inputfile = open('userInformation.txt','r')
            next(inputfile)    
            line_lists = inputfile.readlines()             
            inputfile.close()
            # search the username
            for x in line_lists:        
                user_line = x.rstrip('\n').split()
                if username in user_line: 
                    catched = True
                    # if found, delete it, then return other username('stranger')
                    username = delete_profile(username)                 
            if catched == False:
                print('No profile under name of', username)
                username = str(input('Please enter your name to load your profile: '))
        # Edit Option       
        elif answer == 2:
            print('Hello', username)
            inputfile = open('userInformation.txt','r')
            next(inputfile)
            line_lists = inputfile.readlines()             
            inputfile.close()
            # search the username        
            for x in line_lists:        
                user_line = x.rstrip('\n').split()
                if username in user_line: 
                    catched = True
                    # if found, Edit it, then return the new username
                    username = edit_profile('userInformation.txt', username)                 
            if catched == False:
                print('No profile under name of', username)
                username = str(input('Please enter your name to Edit your profile: '))
    # Return username to the main module    
    return username
