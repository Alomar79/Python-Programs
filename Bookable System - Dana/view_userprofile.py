# print user profile
def print_profile(fileName , username):
    inputfile = open(fileName,'r')
    next(inputfile)    
    records = inputfile.readlines() 
    found = False
    # while loop until find the profile
    while found ==False:
        for x in records:        
            record_list = x.rstrip('\n').split()
            if username in record_list:
                found = True
        if found == False:
            print('There is no profile under the name', username)
            username = str(input("Please enter your name to load your profile: "))   
    # printing information
    for x in records:        
        record_list = x.rstrip('\n').split()
        if username in record_list:
            print('+-----------------------+')
            print('|+---------------------+|')
            print('|| {0:20}||'.format(username + '\'s Profile'))
            print('|+---------------------+|')
            print('+-----------------------+')
            print('\nJoin Date            : ',record_list[0])                
            print('Date of Birth        : ',record_list[2])
            print('Age                  : ',record_list[3])
            print('Gender               : ',record_list[4])
            print('Budget per book      : ',record_list[5])
            print('Favorite medium      : ',record_list[6])
            print('Favorite genres      : ',record_list[7])
            print('Edit Date            : ',record_list[8])
            found = True
            break
    inputfile.close()
    return username  

# display user profile
def view_userprofile(username):
    import os
    if os.path.exists('userInformation.txt'):
        # calling function to print user profile information
        username = print_profile('userInformation.txt', username)
        return username        
    else:
        # if the file not found
        print('the file not exist !')
    return username
    