import os
import random
import datetime
import edit_delete_userprofile
import create_load_profile

# print Menu
def menu():
    print("You can perform the following tasks:\n")
    print("\n1) Generate recipes randomly")
    print("2) Generate recipes randomly based on your caloric needs")
    print("3) Generate recipes randomly based on food allergies")
    print("4) Generate recipes randomly based on caloric needs and food allergies\n")

def showImage2(url):
    from PIL import Image
    import requests
    from io import BytesIO
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

def showImage1(url):
    import matplotlib.pyplot as plt 
    import matplotlib.image as mpimg 
    import numpy as np    
    image = mpimg.imread(url) 
    plt.imshow(image) 
    

def showImage3(url):
    import requests, io
    import matplotlib.pyplot as plt 
    response = requests.get(url).content
    img = plt.imread(io.BytesIO(response), format='JPG')
    plt.imshow(img)
    

# read recipes from the file
def read_recipes_file(filename):    
    ifile = open(filename,'r')
    next(ifile)
    recipes_Lst = []
    line = ifile.readline().rstrip()
    while line != '':
        line_list = line.strip().split(';')
        recipes_Lst.append(line_list)
        line = ifile.readline().rstrip()
    ifile.close()
    return recipes_Lst
    
# Print all information of recipe 
def print_recipe_information(line, line_number):
    # make a list from ingredients, which is at index 7 in recipe.csv
    lst = list(line[7].split(","))
    Ingredients = ""
    for n in lst:
        Ingredients +="- " + n + "\n"
    print("\nRandomly generated Recipe #" , line_number)
    print("===========================")    
    print( line[1])
    print(line[9] , "calories.\n")
    ask = (str(input("Are you interested in viewing this recipe? (Y/N):"))).lower()
    if ask == 'y':       
        print("\nRecipe Name: \n" , line[1])
        print("\nTotal alories\n:" , line[9] )
        print("\nTotal Serving \n: ", line[10] )
        print("\nprep time : \n", line[4] )
        print("\ncook time : \n", line[5] )
        print("\nTotal time. : \n", line[6] )
        print("\nimage : ",  showImage2(line[11]))
        print("\nIngredients : \n", Ingredients ) 
        print("\nDirections.. : \n", line[8] )

# Generate recipes Randomly
def generate_random_recipes( number_of_recipes , recipes_Lst):    
    generated_recipes = []
    for i in range(number_of_recipes):
        answer = " "
        while answer != "y":
            # get random number between 1 and length of list
            random_record_no = random.randint(1 , len(recipes_Lst)-1)
            # get the recipe in the index which is generated randomly
            recipe = recipes_Lst[random_record_no]
            #Display information for the recipe numered by line number
            print_recipe_information(recipe , i+1)
            answer = (str(input("Do you want to save this recipe? (Y/N):"))).lower()
            # Save recipe in the list
            if answer == "y":
                generated_recipes.append(recipe)        
    return generated_recipes

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

# get the sum of calories
def total_calories(recipes_Lst):
    total = 0
    for x in recipes_Lst:
        # calculate sum for the field#9, which is the calories
        total += float(x[9])
    return total

# store generated recipes in a file with name: 'username-recipes.txt'
def save_generated_recipes(generated_recipes , username):
    filename = str(username) + "-recipes.txt"
    # header names for the file
    header_str = "Sesion_Date \t Recipe_Name \t Total_Calories \t average_calories\n"
    # get the sum of calories
    calories_sum = round(total_calories(generated_recipes),2)
    counter = 0
    recipes_names = ""
    # prepare a list contains the recipes names
    for x in generated_recipes:
        counter +=1
        if recipes_names != "":
            recipes_names += ","        
        recipes_names += x[1] 
    # calculate the calories average
    average_calories = round(calories_sum / counter, 2)
    recipe_information = the_date()+" ; "+recipes_names+" ; "+str(calories_sum)+" ; "+str(average_calories)

    if not os.path.exists(filename):
        # open file first time
        out = open(filename, "w")
        out.write(header_str)
    
    # open file to append new info    
    out = open(filename, "a")
    out.write(recipe_information + '\n')
    out.close()
    print("\n", counter , "Recipes generated successfully ! \n")
    is_recipes_generated = True
    return is_recipes_generated

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

# Calculate BMR value
def compute_BMR(gender , weight, height , age):
    if gender =='female':
        bmr = 655.1 +(9.563* float(weight)) +(1.85* float(height)*100)-(4.676 * float(age))
    else:
        bmr = 66.47 +(13.75* float(weight)) +(5.003* float(height)*100)-(6.755 * float(age))
    bmr = float(format(bmr , '.2f'))
    return bmr

# get user allergies
def read_user_allergies(username):
    # get list of user info
    user_line_list = read_user_information(username)
    # allergies will be at index 12 in 'userinformation.txt'
    allergies = user_line_list[12]
    return allergies

# Get 'TEE' value
def get_TEE(username):
    # get list of user info
    rec = read_user_information(username)
    # TEE will be at index 11 in 'userinformation.txt'
    TEE = float(rec[11])
    return TEE

# control function: generate recipes,
# and return True if generating success
def generate_recipe_recommendations(username , is_recipes_generated):
    if username == "stranger" or username == "None":
        print("No username under the name: " , username)
        username = create_load_profile.create_load_profile(username)
        return username , False
    print("Hello" , username)
    # print the menu
    menu()
    # bring all recipes to a list
    recipes_Lst = read_recipes_file("recipes.csv")
    choice = int(input("Choose task number to perform: "))
    #Generate recipes randomly
    if choice == 1:
        # Entering number of recipes need to generate
        number_of_recipes = int(input("how many recipes to generate [4 - 6]: "))
        while number_of_recipes not in range(4 , 7):
            number_of_recipes = int(input("how many recipes to generate [4 - 6]: "))
        # if recipes generated, then you can't generate again until close and open again
        if is_recipes_generated == True:
            print("\nYou generated recipes for current session. !")
        else:
            # call function to generate random recipes
            generated_recipes = generate_random_recipes(number_of_recipes , recipes_Lst)
            # Save generated recipes and return 'True' for this session
            is_recipes_generated = save_generated_recipes(generated_recipes, username)
    
    #Generate recipes randomly based on your caloric needs
    elif choice == 2:
        number_of_recipes = int(input("how many recipes to generate [4 - 6]: "))
        while number_of_recipes not in range(4 , 7):
            number_of_recipes = int(input("how many recipes to generate [4 - 6]: "))
        # compute TEE by function
        TEE = get_TEE(username)
        #Calculate caloric needs
        caloric_needs = TEE / number_of_recipes
        cal_needs_recipes = []
        # save in list, all recipes that has a caloric less than or equal caloric needs
        for x in recipes_Lst:
            if float(x[10]) <= caloric_needs:
                cal_needs_recipes.append(x)
        
        if is_recipes_generated == True:
            print("\nYou generated recipes for current session. !")
        else:
            # call function to generate random recipes
            generated_recipes = generate_random_recipes(number_of_recipes , cal_needs_recipes)
            # Save generated recipes and return 'True' for this session
            is_recipes_generated = save_generated_recipes(generated_recipes, username)
    
    #Generate recipes randomly based on food allergies
    elif choice == 3:
        number_of_recipes = int(input("how many recipes would you like to generate (4 , 6): "))
        while number_of_recipes not in range(4 , 7):
            number_of_recipes = int(input("how many recipes would you like to generate (4 , 6): "))        
        # bring user allergies
        Allergies = read_user_allergies(username)
        if Allergies == "-":
            print("\nYou can't generate meals based on food allergies")
            edit_delete_userprofile.edit_delete_profile(username)
        else:
            allergies = Allergies.split(",")
            recipes_not_allergic_to = []
            # save in list, all recipes that is not allergies
            for x in recipes_Lst:
                if x[1] not in allergies:
                    recipes_not_allergic_to.append(x)
            
            if is_recipes_generated == True:
                print("\nYou generated recipes for current session. !")
            else:
                # call function to generate random recipes
                generated_recipes = generate_random_recipes(number_of_recipes , recipes_not_allergic_to)
                # Save generated recipes and return 'True' for this session
                is_recipes_generated = save_generated_recipes(generated_recipes, username)
    
    #Generate recipes randomly based on caloric needs and food allergies
    elif choice == 4:
        number_of_recipes = int(input("how many recipes to generate [4 - 6]: "))
        while number_of_recipes not in range(4 , 7):
            number_of_recipes = int(input("how many recipes to generate [4 - 6]: "))        
        # bring user allergies
        Allergies = read_user_allergies(username)
        if Allergies == "-":
            print("\nYou can't generate meals based on food allergies")
            edit_delete_userprofile.edit_delete_profile(username)
        else:
            allergies = Allergies.split(",")
            # save recipes but not allergic to
            recipes_not_allergic_to = []
            # save in list, all recipes that is not allergies
            for x in recipes_Lst:
                if x[1] not in allergies:
                    recipes_not_allergic_to.append(x)
            # compute TEE by function
            TEE = get_TEE(username)
            #Calculate caloric needs
            caloric_needs = TEE / number_of_recipes
            cal_needs_allergies_recipes = []
            # save in list, all recipes that has a caloric less than or equal caloric needs
            # and are not allergies
            for x in recipes_not_allergic_to:
                if float(x[10]) <= caloric_needs:
                    cal_needs_allergies_recipes.append(x)

            if is_recipes_generated == True:
                print("\nYou generated recipes for current session. !")
            else:
                # call function to generate random recipes
                generated_recipes = generate_random_recipes(number_of_recipes , cal_needs_allergies_recipes)
                # Save generated recipes and return 'True' for this session
                is_recipes_generated = save_generated_recipes(generated_recipes, username)
    # return true if recipes generated    
    return username , is_recipes_generated



    



