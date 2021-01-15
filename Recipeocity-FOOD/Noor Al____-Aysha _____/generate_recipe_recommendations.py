import os.path
import edit_or_delete_userprofile
import create_or_load_userprofile

#print the menu
def display_menu():
    print("You can perform the following tasks:\n")
    print("\n1) Generate recipes randomly")
    print("2) Generate recipes randomly based on your caloric needs")
    print("3) Generate recipes randomly based on food allergies")
    print("4) Generate recipes randomly based on caloric needs and food allergies\n")

# get recipes from the file recipes.csv
def read_recipes(CSV_FILENAME):    
    infile = open(CSV_FILENAME,'r')
    next(infile)
    recipes_list = []
    line = infile.readline().rstrip()
    counter = 1
    while line != '':
        line_list = line.strip().split(';')
        recipes_list.append(line_list)
        counter +=1
        line = infile.readline().rstrip()
    infile.close()
    return recipes_list

def show_image(url):
    print("url")
    
# print recipe details
def display_recipe(recipe, Num):
    lst = list(recipe[7].split(","))
    Ingredients = ""
    for n in lst:
        Ingredients +="- " + n + "\n"
    print("\nRandomly generated Recipe #" , Num)
    print("===========================")
    print( recipe[1])
    print(recipe[9] , "calories.\n")
    ask = (str(input("Are you interested in viewing this recipe? (Y/N):"))).lower()
    if ask == 'y':       
        print("\nRecipe Name: \n" , recipe[1])
        print("\nTotal alories:" , recipe[9] )
        print("\nTotal Serving : ", recipe[10] )
        print("\nprep time : ", recipe[4] )
        print("\ncook time : ", recipe[5] )
        print("\nTotal time. : ", recipe[6] )
        print("\nimage : ",  show_image(recipe[11]))
        print("\nIngredients : \n", Ingredients ) #recipe[7]
        print("\nDirections.. : \n", recipe[8] )

# generate user recipes randomly 
def generate_random_recipes( recipes_count , recipes_list):
    import random
    # recipes_list = read_recipes(CSV_FILENAME)    
    generated_recipes = []
    for i in range(recipes_count):
        ans = " "
        while ans != "y":
            random_record = random.randint(1 , len(recipes_list)-1)
            recipe = recipes_list[random_record]
            display_recipe(recipe , i+1)
            ans = (str(input("\nDo you want to save this recipe? (Y/N):"))).lower()
            if ans == "y":
                generated_recipes.append(recipe)
        
    return generated_recipes

def date_now():
    import datetime
    x = datetime.datetime.now()
    thisDay = x.strftime("%d")
    thisMonth = x.strftime("%m")
    thisYear = x.strftime("%Y")
    thisHour = x.strftime("%H")
    thisMinute = x.strftime("%M")
    thisSecond = x.strftime("%S")
    thisdate = thisDay+'/'+thisMonth+'/'+thisYear+','+thisHour+':'+thisMinute+':'+thisSecond
    return thisdate

def total_calories(recipes):
    sum = 0
    for x in recipes:
        sum += float(x[9])
    return sum

# Write generated recipes to the file
def save_generated_recipes(generated_recipes , username):
    filename = str(username) + "-recipes.txt"
    #outfile = open(filename,"w")
    header = "Sesion_Date \t Recipe_Name \t Total_Calories \t Average_calories\n"
    totalCalories = round(total_calories(generated_recipes),2)
    counter = 0
    recipes_names = ""
    for x in generated_recipes:
        counter +=1
        if recipes_names != "":
            recipes_names += ","        
        recipes_names += x[1] 
    average_cal = round(totalCalories/counter,2)
    recipe_info = date_now()+"\t"+recipes_names+"\t"+str(totalCalories)+"\t"+str(average_cal)

    if not os.path.exists(filename):
        out = open(filename, "w")
        out.write(header)
    
    # open file to append new info    
    out = open(filename, "a")
    out.write(recipe_info + '\n')
    out.close()
    print("\n", counter , "Recipes generated successfully ! \n")
    is_session_recipes_generated = True
    return is_session_recipes_generated

# Read profile information from the file
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

def BMR_calculate(gender , Weight, Height , Age):
    if gender =='female':
        BMR = 655.1 +(9.563* float(Weight)) +(1.85* float(Height)*100)-(4.676 * float(Age))
    else:
        BMR = 66.47 +(13.75* float(Weight)) +(5.003* float(Height)*100)-(6.755 * float(Age))
    BMR = float(format(BMR , '.2f'))
    return BMR

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

# get allergies from userInformation,txt
def read_user_allergies(username):
    record_list = read_information(username)
    allergies = record_list[12]
    return allergies

def bring_TEE(username):
    
    record = read_information(username)    
    TEE = float(record[11])
    return TEE

# generate recipe recommendations for the user
def generate_recipe_recommendations(username , is_session_recipes_generated):
    if username == "stranger" or username == "None":
        print("No username under the name: " , username)
        username = create_or_load_userprofile.create_or_load_profile(username)
        return username , False
    print("Hello" , username)
    display_menu()
    recipes_list = read_recipes("recipes.csv")
    choice = int(input("Choose task number to perform: "))
    if choice == 1:
        recipes_count = int(input("how many recipes would you like to generate (4 , 6): "))
        while recipes_count not in range(4 , 7):
            recipes_count = int(input("how many recipes would you like to generate (4 , 6): "))
        if is_session_recipes_generated == True:
            print("\nYou generated their recipes for the current session. !")
        else:
            generated_recipes = generate_random_recipes(recipes_count , recipes_list)
            is_session_recipes_generated = save_generated_recipes(generated_recipes, username)
    
    elif choice == 2:
        recipes_count = int(input("how many recipes would you like to generate (4 , 6): "))
        while recipes_count not in range(4 , 7):
            recipes_count = int(input("how many recipes would you like to generate (4 , 6): "))
        TEE = bring_TEE(username)
        caloric_needs = TEE / recipes_count
        cal_needs_recipes = []
        for x in recipes_list:
            if float(x[10]) <= caloric_needs:
                cal_needs_recipes.append(x)
        
        if is_session_recipes_generated == True:
            print("\nYou generated their recipes for the current session. !")
        else:
            generated_recipes = generate_random_recipes(recipes_count , cal_needs_recipes)
            is_session_recipes_generated = save_generated_recipes(generated_recipes, username)
    
    elif choice == 3:
        recipes_count = int(input("how many recipes would you like to generate (4 , 6): "))
        while recipes_count not in range(4 , 7):
            recipes_count = int(input("how many recipes would you like to generate (4 , 6): "))        
        Allergies = read_user_allergies(username)
        if Allergies == "-":
            print("\nYou cannot generate meals based on food allergies")
            edit_or_delete_userprofile.edit_or_delete_profile(username)
        else:
            allergies = Allergies.split(",")
            not_allergies_recipes = []
            for x in recipes_list:
                if x[1] not in allergies:
                    not_allergies_recipes.append(x)
            
            if is_session_recipes_generated == True:
                print("\nYou generated their recipes for the current session. !")
            else:
                generated_recipes = generate_random_recipes(recipes_count , not_allergies_recipes)
                is_session_recipes_generated = save_generated_recipes(generated_recipes, username)
    
    elif choice == 4:
        recipes_count = int(input("how many recipes would you like to generate (4 , 6): "))
        while recipes_count not in range(4 , 7):
            recipes_count = int(input("how many recipes would you like to generate (4 , 6): "))        
        Allergies = read_user_allergies(username)
        if Allergies == "-":
            print("\nYou cannot generate meals based on food allergies")
            edit_or_delete_userprofile.edit_or_delete_profile(username)
        else:
            allergies = Allergies.split(",")
            not_allergies_recipes = []
            for x in recipes_list:
                if x[1] not in allergies:
                    not_allergies_recipes.append(x)
            
            TEE = bring_TEE(username)
            caloric_needs = TEE / recipes_count
            cal_needs_allergies_recipes = []
            for x in not_allergies_recipes:
                if float(x[10]) <= caloric_needs:
                    cal_needs_allergies_recipes.append(x)

            if is_session_recipes_generated == True:
                print("\nYou generated their recipes for the current session. !")
            else:
                generated_recipes = generate_random_recipes(recipes_count , cal_needs_allergies_recipes)
                is_session_recipes_generated = save_generated_recipes(generated_recipes, username)
        
    return username, is_session_recipes_generated



    



