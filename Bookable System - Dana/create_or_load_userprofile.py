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
   
def read_genres(CSV_FILENAME):
    infile = open(CSV_FILENAME,'r')
    next(infile)
    genres_list = []
    genres_names_list = []
    genres_numbers_list = []
    all_lines = infile.readlines()    
    for x in all_lines:        
        line_list = x.strip().split(';')
        genres_list.append(str(line_list[1]) +'\t\t'+ str(line_list[0]))
        genres_names_list.append(line_list[0])
        genres_numbers_list.append(int(line_list[1]))
    infile.close()
    return genres_list , genres_names_list , genres_numbers_list
    
def create_profile():        
    import datetime
    Name = str(input('Enter your name please:'))
    DOB = str(input('Enter your birth date as follows(dd/mm/yyyy) : '))
    Gender = (str(input('Enter your gender please( male / female) :'))).lower()
    budget = float(input('Enter budget per book in Qatari Riyal (more than QAR12 ):'))
    while budget < 12:
        budget = float(input('Enter budget per book in Qatari Riyal (more than QAR12 ):'))
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


    x = datetime.datetime.now()
    thisDay = x.strftime("%d")
    thisMonth = x.strftime("%m")
    thisYear = x.strftime("%Y")
    thisHour = x.strftime("%H")
    thisMinute = x.strftime("%M")
    thisSecond = x.strftime("%S")
    Joindate = thisDay+'/'+thisMonth+'/'+thisYear+','+thisHour+':'+thisMinute+':'+thisSecond
    
    
    birth_list = DOB.split('/')
    year_of_birth = int(birth_list[2])
    Age = int(thisYear) - year_of_birth
    
    # call function to display genres
    genres_list , genres_names, genres_numbers = read_genres('genres.csv')
    print('\n\t Genres List')
    print('\n\t ===============')
    print("\nGenres number \t Genres name\n")
    for x in genres_list:
        print(x)
    genres = ''   # string variable to store genres 
    genre_num = int(input('Enter genre# that you want(-1 to finish): '))
    while genre_num != -1:
        if genre_num in genres_numbers:
            index = genres_numbers.index(genre_num)
            if genres !='':
                genres += ','
            genre = (genres_names[index]).replace(' ' , '_')
            genres += genre
        else:
            print('\nWrong input!, select again\n')
        genre_num = int(input('Enter genre# that you want(-1 to finish): '))
    if genres =='':
        genres = '-'
    
    header_string = "JoinDate \t\t Name  \tBirthYear\t Age" \
        +"\tGender \t  Budget \t  Medium   \t Genres  \t Edit Date \n"
    
    EditDate = '-'
    user_information = Joindate+'\t'+Name+'\t'+ str(year_of_birth) +'\t'+ str(Age) +'\t'\
    + Gender +'\t'+ str(budget) +'\t'+ medium + '\t' + genres +'\t'+ EditDate
    
    # call function to write information to the file
    writeToFile('userInformation.txt' , header_string , user_information)
    print('\nProfile for user',Name,'is created and loaded successfully.\n')
    return Name


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
    
