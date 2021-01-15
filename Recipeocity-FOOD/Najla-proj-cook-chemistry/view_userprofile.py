
# prepare activity level  
def return_activity_level(acc_number):
    activity = int(acc_number)
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
# Print user profile information depend on line list
def print_user_fields(userline):
    print('---------------------------')
    print('Join Date : ',userline[0])                
    print('Year of Birth : ',userline[4])
    print('Age  : ',userline[5])
    print('Gender   : ',userline[6])
    print('Height (m) : ',userline[2])
    print('Weight (kg)  : ',userline[3])
    print('Body Mass Index (BMI) : ',userline[7])
    print('BMI Range  : ',userline[8])
    print('Basal Metabolic Rate (BMR) : ',userline[9])
    print('Activity level  : ',return_activity_level(userline[10]))
    print('Total Energy Expenditure(TEE): ',userline[11])
    print('Food Allergies  : ',userline[12])
    print('Edit Date  : ',userline[13])

# print profile information
def displsy_user_profile_info(fileName , username):
    inputfile = open(fileName,'r')
    next(inputfile)    
    records = inputfile.readlines() 
    found = False
    while found ==False:
        # search about username
        for x in records:        
            userline = x.rstrip('\n').split()
            if username in userline:
                found = True
        if found == False:
            print('There is no profile under the name', username)
            username = str(input("Please enter your name to load your profile: "))   
    
    # Print all user profile information
    for element in records:        
        userline = element.rstrip('\n').split()
        if username in userline:
            print( username + '\'s Profile')
            print_user_fields(userline)            
            break
    inputfile.close()
    return username  

# Control function in the Module: view user profile information
def view_userprofile(username):
    import os
    # if the file exist, then print user information
    if os.path.exists('userInformation.txt'):
        username = displsy_user_profile_info('userInformation.txt', username)
        return username        
    else:
        print('the file not exist !')
    return username
    