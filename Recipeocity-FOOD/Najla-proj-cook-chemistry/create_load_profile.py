import os.path

   
#Read ingredients file
def read_ingredients_from_file(filename):
    inputfile = open(filename,'r')
    next(inputfile)
    ingredients = []
    ingredients_names = []
    ingredients_numbers = []
    linees = inputfile.readlines()    
    for x in linees:        
        record = x.rstrip().split(';')
        ingredients.append(str(record[1]) +'\t\t'+ str(record[0]))
        ingredients_names.append(record[0])
        ingredients_numbers.append(int(record[1]))
    inputfile.close()
    # return 3 lists
    return ingredients , ingredients_names , ingredients_numbers

# save person in the file
def write(fileName, header , user_info ):   
    # Display header file
    if not os.path.exists(fileName):
        out = open(fileName, "w")
        out.write(header)
    # Add new person to file   
    out = open(fileName, "a")
    out.write(user_info + '\n')
    out.close()

# prepare join date from the system
def take_joindate():
    import datetime
    dt = datetime.datetime.now()
    day = dt.strftime("%d")
    month = dt.strftime("%m")
    year = dt.strftime("%Y")
    hour = dt.strftime("%H")
    minute = dt.strftime("%M")
    sec = dt.strftime("%S")
    Joindate = day+'/'+month+'/'+year+','+hour+':'+minute+':'+sec
    return Joindate

def bring_BMI_range(BMI):    
    if BMI < 18.5:
        BMIRange = 'Underweight'
    elif BMI>= 18.5 and BMI <=24.9:
        BMIRange = 'Normal'
    elif BMI>= 25.0 and BMI <=29.9:
        BMIRange = 'Overweight'
    elif BMI>= 30.0:
        BMIRange = 'Obese'
    return BMIRange

#print activitu menu 
def activity_menu():
    print('Which one of the following statements describes your activity level?')
    print("\n1) Little/No exercise")
    print("2) Light exercise")
    print("3) Moderate exercise (3-5 days/week)")
    print("4) Very active (6-7 days/week)")
    print("5) Extra active (very active & physical job)\n")

# calculate activity value depend on activity number
def prepare_activity_value(Activity):
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

def display_ingredients_and_prepare_allergies():
    # bring ingredients
    ingredients, ingredient_names, ingredient_numbers = read_ingredients_from_file('ingredients.csv')
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

#prepare activity_level depend on activity_number
def return_activity_level(activity_number):
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

# prepare information and calculatings to create user profile
def create_profile():        
    import datetime    
    Joindate = take_joindate()
    Name = str(input('Enter your name please:'))    
    Height = float(input('Enter your height(in meters) :'))
    Weight = float(input('Enter your weight(in kilograms) :'))
    Gender = (str(input('Enter your gender pleas( male / female) :'))).lower()
    birthyear = int(input('Enter year of birth as follows(yyyy) : '))
    indx = Joindate.index(',')
    jdate = Joindate[0:indx]
    date = jdate.split('/')
    thisYear = date[2]
    # compute the age
    Age = int(thisYear) - birthyear
    BMI = float(format(Weight / (Height**2) , '.2f'))
    # prepare BMI Range 
    BMIRange = bring_BMI_range(BMI)    
    # calculate BMR
    if Gender =='female':
        BMR = 655.1 +(9.563* Weight) +(1.85* Height*100)-(4.676 * Age)
    else:
        BMR = 66.47 +(13.75* Weight) +(5.003* Height*100)-(6.755 * Age)
    BMR = float(format(BMR , '.2f'))    
    # print activity menu
    activity_menu()
    # Ask to enter activity number
    Activity = int(input("Please Enter number that describes your activity level from the list above: "))
    # validate activity choice
    while Activity not in range(1,6):
        Activity = int(input("Please Enter number that describes your activity level from the list above: "))
    
    activity_val = prepare_activity_value(Activity)
    
    TEE = format(BMR * activity_val , '.2f')
    
    # call function to display ingredients
    Allergies = display_ingredients_and_prepare_allergies()    
    
    header = "Join Date  \t  Name \tHeight\tWeight\tBirthYear\tAge"\
        +"\tGender\tBMI\tBMI-range\tBMR\tActivity\tTEE\tAllergies\tEdit Date \n"
    
    EditDate = '-'
    # prepare information as string
    user_information = Joindate+'\t'+Name+'\t'+str(Height)+'\t'+str(Weight)+'\t'\
        + str(birthyear) +'\t'+ str(Age) +'\t'+ Gender +'\t'+ str(BMI) +'\t'+ BMIRange +'\t'+ str(BMR) +'\t'\
        + str(Activity) +'\t'+ str(TEE) +'\t'+ Allergies +'\t'+ EditDate
    
    # write information to the file
    write('userInformation.txt' , header , user_information)
    print('\nProfile for user',Name,'is crated and loaded successfully.\n')
    return Name

def display_user_information(records, username):
    # loop to print user information
    for line in records:        
        record_list = line.rstrip('\n').split()
        if username in record_list:           
            print(username + '\'s Profile')
            print('|+---------------------+|\n')            
            print('\nJoin Date: ',record_list[0])                
            print('Date of Birth: ',record_list[4])
            print('Age : ',record_list[5])
            print('Gender : ',record_list[6])
            print('Height (m) : ',record_list[2])
            print('Weight (kg)  : ',record_list[3])
            print('Body Mass Index (BMI) : ',record_list[7])
            print('BMI Range   : ',record_list[8])
            print('Basal Metabolic Rate (BMR)   : ',record_list[9])
            print('Activity level   : ',return_activity_level(record_list[10]))
            print('Total Energy Expenditure(TEE): ',record_list[11])
            print('Food Allergies   : ',record_list[12])
            #found = True
            break
    
# load profile depend on username
def load_profile(fileName , username):
    inputfile = open(fileName,'r')
    next(inputfile)
    records = inputfile.readlines()
    found = False
    # search about username
    while found ==False:
        for x in records:
            record_list = x.rstrip('\n').split()
            if username in record_list:
                found = True
        if found == False:
            print('There is no profile under : ', username)
            username = str(input("Enter User Name to load your profile: "))
    # print user information
    display_user_information(records, username)
    
    inputfile.close()
    return username   
    
# first function in the module
# to create or load profile    
def create_load_profile(username):
    if os.path.exists('userInformation.txt'):
        answer = (str(input("Do you create profile before? (Y/N): "))).lower()
        while answer !='y' and answer !='n':
            answer = (str(input("Do you create profile before? (Y/N): "))).lower()
        # if user has a profile, then load it
        if answer=='y':
            username = load_profile('userInformation.txt', username)
            return username
        elif answer=='n':
            # create new profile
            print('please create a new profile\n')
            username = create_profile()
            answer2 = (str(input('Do you want to view your profile information?(Y/N)'))).lower()
            if answer2 == 'y':
                load_profile('userInformation.txt', username)
            return username
    else:
        # if the file not exist, then create new profile
        username = create_profile()
        return username
    return username
    
