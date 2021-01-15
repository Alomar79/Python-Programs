import os
import create_or_load_userprofile
import datetime

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
                user_line[8] = edit_date()
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

# Read genrees from the file 'userInformation.txt'
def read_new_genrees():
    # read genres using create_load_profile module
    genres , genre_names, genre_nums = create_or_load_userprofile.read_genres('genres.csv')
    print('\n\t genres List')
    print('\n\t ============')
    print("\ngenre number \t genre name\n")
    for x in genres:
        print(x)
    genrees = ''   # to store genrees 
    # Read genre number that the user you want
    genre_no = int(input('Enter genre# that you want(-1 to finish): '))
    while genre_no != -1:
        if genre_no in genre_nums:
            index = genre_nums.index(genre_no)
            if genrees !='':
                genrees += ','
            genre = (genre_names[index]).replace(' ' , '_')
            genrees += genre
        else:
            print('\nWrong !, select again\n')
        genre_no = int(input('Enter genre# that you want(-1 to finish): '))
    if genrees =='':
        genrees = '-'
    return genrees

# display Edit Menu
def print_edit_menu():
    print('These are the fields that you can edit in your profile:')    
    print('1) Name')
    print('2) Date of Birth (dd/mm/yyyy')
    print('3) Gender')
    print('4) Budget')
    print('5) Medium')
    print('6) Favorite genres')

# Edit profile Function
def edit_profile(filename , username):
    choice = 0
    # Print Edit Menu
    print_edit_menu() 
    # Ask to Enter the choice   
    choice = int(input('Enter a number to select a field to edit:'))
    # Read user information and return line as list
    line_list = read_user_information(username)
    if choice == 1:
        new_name = str(input('Enter your new name:'))
        # change the information by the function :
        # change_user_information(oldVal , newVal, username)
        username = change_user_information(username , new_name, username)
    # Edit Year and other relatives
    if choice == 2:
        birth_year = str(input('Enter your birth year as follows(yyyy) : '))        
        #birthDate = birth_year.split('/')
        x = datetime.datetime.now()
        thisYear = x.strftime("%Y")
        #year_of_birth = int(birthDate[2])
        Age = int(thisYear) - int(birth_year)
        # call function to change the values
        change_user_information(line_list[2] , birth_year ,username)
        change_user_information(line_list[3] , Age ,username)
    # Edit gender and other relatives
    if choice == 3:
        new_gender = (str(input('Enter your gender(male / female) : '))).lower()
        # call function to change the values
        change_user_information(line_list[4] , new_gender ,username)
    # Edit height and other relatives   
    if choice == 4:
        new_budget = float(input('Enter budget per book in Qatari Riyal (more than QAR12 ):'))
        # call function to change the values
        change_user_information(line_list[5] , new_budget ,username)
    # Edit weight and other relatives
    if choice == 5:
        print('list of possible reading mediums to choose from')
        print('1) Printed (i.e., physical books)')
        print('2) Digital (i.e., E-books)')
        print('3) Both digital and physical books')
        mediums_dict =	{
            1: "physical-books",
            2: "E-books",
            3: "Both-digital-and-physical-books"
        }
        Medium_number = int(input('Enter your choice:'))
        medium = mediums_dict[Medium_number]
        # call function to change the values
        change_user_information(line_list[6] , medium ,username)
    
    # Edit genrees
    if choice == 6:
        genrees = read_new_genrees()
        # call function to change the genrees
        change_user_information(line_list[7] , genrees ,username)
        
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
