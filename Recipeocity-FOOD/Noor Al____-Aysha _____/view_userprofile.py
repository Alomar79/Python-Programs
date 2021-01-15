    
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

def print_profile(fileName , username):
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
            print('Edit Date                    : ',record_list[13])
            found = True
            break
    inputfile.close()
    return username  

def view_userprofile(username):
    import os
    if os.path.exists('userInformation.txt'):
        username = print_profile('userInformation.txt', username)
        return username        
    else:
        print('the file not exist !')
    return username
    