import os.path
import random
import datetime
import edit_or_delete_userprofile
import create_or_load_userprofile

# print Menu
def menu():
    print("You can perform the following tasks:\n")
    print("\n1) Generate books randomly")
    print("2) Generate books randomly based on budget")
    print("3) Generate books randomly based on genre(s)")
    print("4) Generate books randomly based on budget and genre(s)\n")

# display image py import PIL
def showImage2(url):
    indx = url.index(',')
    url_link = url[0:indx]

    from PIL import Image
    import requests
    from io import BytesIO
    response = requests.get(url_link)
    img = Image.open(BytesIO(response.content))
    print(url_link)
    img.show()

def showImage5(url):
    import matplotlib.pyplot as plt 
    import matplotlib.image as mpimg 
    import numpy as np    
    image = mpimg.imread(url) 
    plt.imshow(image)    

def showImage6(url):
    import requests, io
    import matplotlib.pyplot as plt 
    response = requests.get(url).content
    img = plt.imread(io.BytesIO(response), format='JPG')
    plt.imshow(img)

# read books from the file
def read_books_file(filename):    
    ifile = open(filename,'r')
    next(ifile)
    books_lst = []
    line = ifile.readline().rstrip()
    while line != '':
        line_list = line.strip().split(';')
        books_lst.append(line_list)
        line = ifile.readline().rstrip()
    ifile.close()
    return books_lst

# prepare session number (retrieved from username-books.txt)
def Sesion_num(filename):
    Sesion_number = 0
    if not os.path.exists(filename):
        Sesion_number = 1
    else:
        ifile = open(filename,'r')
        next(ifile)
        line = ifile.readline().rstrip()
        while line != '':
            Sesion_number += 1
            line = ifile.readline().rstrip()
    return Sesion_number



# Print all information of book 
def print_book_information(line, line_number):
    # make a list from genres, which is at index 4 in books.csv
    lst = list(line[4].split(","))
    genres = ""
    for n in lst:
        genres +="- " + n + "\n"
    print("\nRandomly generated books #" , line_number)
    print("===========================")    
    print( line[1])
    print( "Price: " , line[6], "$\n")
    ask = (str(input("Are you interested in seeing this book? (Y/N):"))).lower()
    if ask == 'y':       
        print("\nbook Title: \n" , line[1])
        print("\nbook author\n:" , line[2] )
        print("\nformat. \n: ", line[5] )
        print("\npublication date : \n", line[8] )
        print("\nbook’s ISBN : \n", line[7] )
        print("\nbook cover image : \n", showImage2(line[11]) )
        print("\nbook’s average rating : ",  line[10])
        print("\nbook price : \n", line[6]  )
        print("\nbook genres : \n", genres )
        print("\nbook description : \n", line[3] )

# Generate books Randomly
def generate_random_books(number_of_books , books_lst):    
    generated_books = []
    for i in range(number_of_books):
        answer = " "
        while answer != "y":
            # get random number between 1 and length of list
            random_record_no = random.randint(1 , len(books_lst)-1)
            # get the book in the index which is generated randomly
            book = books_lst[random_record_no]
            #Display information for the book numered by line number
            print_book_information(book , i+1)
            answer = (str(input("Do you want to save this book? (Y/N):"))).lower()
            # Save book in the list
            if answer == "y":
                generated_books.append(book)        
    return generated_books

# Get the Date and time now
def the_date():    
    dt = datetime.datetime.now()
    day = dt.strftime("%d")
    month = dt.strftime("%m")
    year = dt.strftime("%Y")
    hour = dt.strftime("%H")
    minute = dt.strftime("%M")
    sec = dt.strftime("%S")
    thisdate = day+'/'+month+'/'+year+'-'+hour+':'+minute+':'+sec
    return thisdate

# get the sum of price
def get_total_prices(books_lst):
    total = 0
    for x in books_lst:
        # calculate sum for the field#6, which is the price
        total += float(x[6])
    return total

# store generated books in a file with name: 'username-books.txt'
def save_generated_books(generated_books , username):
    filename = str(username) + "-books.txt"
    # header names for the file
    header_str = "Sesion_num \t book_Title \t total-prices \t average_prices\n"
    # get the sum of prices
    total_price = round(get_total_prices(generated_books),2)
    counter = 0
    books_names = ""
    # prepare a list contains the books names
    for x in generated_books:
        counter +=1
        if books_names != "":
            books_names += ","        
        books_names += x[1] 
    # calculate the average of prices
    avg_prices = round(total_price / counter, 2)
    Sesion_number = Sesion_num(filename)
    # prepare information string to write it to the file
    book_information = str(Sesion_number)+" ; "+books_names+" ; "+str(total_price)+" ; "+str(avg_prices)

    # if the file not found, then create it and write the header names 
    if not os.path.exists(filename):
        # open file first time
        out = open(filename, "w")
        out.write(header_str)
    
    # open file to append new info    
    out = open(filename, "a")
    out.write(book_information + '\n')
    out.close()
    print("\n", counter , "books generated successfully ! \n")
    is_books_generated = True
    return is_books_generated

# Read user information and return a list
def read_user_information(username):
    user_line_list = []
    inputfile = open('userInformation.txt','r')
    next(inputfile)    
    records = inputfile.readlines() 
    found = False
    # search about the username
    while found ==False:
        for x in records:        
            user_line_list = x.rstrip('\n').split()
            if username in user_line_list:
                found = True
                return user_line_list
    return user_line_list 

# get budget field from userInformation.txt file
def get_budget_from_userInformation(username):
    user_line_list = read_user_information(username)
    budget = float(user_line_list[5])
    return budget
    
# get user agenres
def read_user_agenres(username):
    # get list of user info
    user_line_list = read_user_information(username)
    #  genres will be at index 7 in 'userinformation.txt'
    agenres = user_line_list[7]
    return agenres

# return True if generating success
def generate_book_recommendations(username , is_books_generated):
    if username == "stranger" or username == "None":
        print("No username under the name: " , username)
        username = create_or_load_userprofile.create_or_load_profile(username)
        return username , False
    print("Hello" , username)
    # print the menu
    menu()
    # bring all books to a list
    books_lst = read_books_file("books.csv")
    choice = int(input("Choose task number to perform: "))
    #Generate books randomly
    if choice == 1:
        # Entering number of books need to generate
        number_of_books = int(input("how many books to generate [5 - 10]: "))
        while number_of_books not in range(5 , 11):
            number_of_books = int(input("how many books to generate [5 - 10]: "))
        # if books generated, then you can't generate again until close and open again
        if is_books_generated == True:
            print("\nYou generated books for current session. !")
        else:
            # call function to generate random books
            generated_books = generate_random_books(number_of_books , books_lst)
            # Save generated books and return 'True' for this session
            is_books_generated = save_generated_books(generated_books, username)
    
    #Generate books randomly based on budget
    elif choice == 2:
        number_of_books = int(input("how many books would you like to generate (5 , 10): "))
        while number_of_books not in range(5 , 11):
            number_of_books = int(input("how many books would you like to generate (5 , 10): "))
        # bring budget
        budget = get_budget_from_userInformation(username)
        budget_books = []
        # save in list, all books that based budget
        for x in books_lst:
            if float(x[6]) <= budget:
                budget_books.append(x)
        
        if is_books_generated == True:
            print("\nYou generated books for current session. !")
        else:
            # call function to generate random books
            generated_books = generate_random_books(number_of_books , budget_books)
            # Save generated books and return 'True' for this session
            is_books_generated = save_generated_books(generated_books, username)
    
    #Generate books randomly based on agenres
    elif choice == 3:
        number_of_books = int(input("how many books would you like to generate (5 , 10): "))
        while number_of_books not in range(5 , 11):
            number_of_books = int(input("how many books would you like to generate (5 , 10): "))        
        # bring user genres
        fav_genres = read_user_agenres(username)
        if fav_genres == "-":
            print("\nYou can't generate books based on genres")
            edit_or_delete_userprofile.edit_delete_profile(username)
        else:
            agenres = fav_genres.split(",")
            books_in_genres = []
            # save in list, all books based on genre(s)
            for x in books_lst:
                if x[1] not in agenres:
                    books_in_genres.append(x)
            
            if is_books_generated == True:
                print("\nYou generated books for current session. !")
            else:
                # call function to generate random books
                generated_books = generate_random_books(number_of_books , books_in_genres)
                # Save generated books and return 'True' for this session
                is_books_generated = save_generated_books(generated_books, username)
    
    #Generate books randomly  based on genre(s) and based on budget
    elif choice == 4:
        number_of_books = int(input("how many books to generate [5 - 10]: "))
        while number_of_books not in range(5 , 11):
            number_of_books = int(input("how many books to generate [5 -10]: "))        
        # bring user genres
        Agenres = read_user_agenres(username)
        if Agenres == "-":
            print("\nYou can't generate books based on favorite genres")
            edit_or_delete_userprofile.edit_delete_profile(username)
        else:
            agenres = Agenres.split(",")
            # save books 
            books_in_genres = []
            # save in list, all books based on genre(s)
            for x in books_lst:
                if x[1] not in agenres:
                    books_in_genres.append(x)
            
            # save in list, all books based on budget
            # and  based on genre(s)
            budget = get_budget_from_userInformation(username)
            budget_genres_books = []
            for x in books_in_genres:
                if float(x[6]) <= budget:
                    budget_genres_books.append(x)

            if is_books_generated == True:
                print("\nYou generated books for current session. !")
            else:
                # call function to generate random books
                generated_books = generate_random_books(number_of_books , budget_genres_books)
                # Save generated books and return 'True' for this session
                is_books_generated = save_generated_books(generated_books, username)
    # return true if books generated    
    return username , is_books_generated



    



