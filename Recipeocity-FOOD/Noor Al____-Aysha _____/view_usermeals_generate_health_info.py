import os
# import edit_or_delete_userprofile
import create_or_load_userprofile
import generate_recipe_recommendations

# read generated user recipes from 'username-recipes.txt'
def read_user_meals(user_recipes_filename):    
    infile = open(user_recipes_filename,'r')
    next(infile)
    user_recipes_list = []
    line = infile.readline().rstrip()
    counter = 1
    while line != '':
        line_list = []
        line_list.append(line[:20])
        line_list.append(line[20:len(line)-13].strip().split(','))
        line_list.append(line[len(line)-13:].strip().split(' '))
        user_recipes_list.append(line_list)
        counter +=1
        line = infile.readline().rstrip()
    infile.close()
    return user_recipes_list

# get recipes from the file
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

# print recipe details
def display_recipe(recipe, Num , servings_size): 
    lst = list(recipe[7].strip().split(","))
    Ingredients = ""
    for n in lst:
        if n != " ":
            Ingredients += "- " + n + "\n"
    print("\nGenerated Recipe #" , Num)
    print("===========================")
    print( recipe[1])
    print(float(recipe[9]) * servings_size , "calories.\n")
    ask = (str(input("Are you interested in viewing this recipe? (Y/N):"))).lower()
    if ask == 'y':       
        print("\nRecipe Name: \n" , recipe[1])
        print("\nTotal alories:" , float(recipe[9]) * servings_size )
        print("\nTotal Serving : ", servings_size )
        print("\nprep time : ", recipe[4] )
        print("\ncook time : ", recipe[5] )
        print("\nTotal time. : ", recipe[6] )
        print("\nimage : ",  generate_recipe_recommendations.show_image(recipe[11]))
        print("\nIngredients : \n", Ingredients ) #recipe[7]
        print("\nDirections.. : \n", recipe[8] )

# plotting calories list
def plot_calories_list(calories_list , session_number):
    import matplotlib.pyplot as plt

    slice_labels = []
    lst = list(range(len(calories_list)))
    for i in lst:
        slice_labels.append("Meal #"+str(i))

    plt.title("Calorie distribution of the meals" \
        +" from session # "+str(session_number)+" (total is"+ str(sum(calories_list))+" calories)")
    plt.pie(calories_list , labels=slice_labels, autopct='%1.2f%%')
    plt.show()

# view usermeals and generate health information
def view_usermeals_generate_health_info(username):
    if username == "stranger" or username == "None":
        print("No username under the name: " , username)
        username= create_or_load_userprofile.create_or_load_profile(username)
        return username

    filename = str(username) + "-recipes.txt"
    if not os.path.exists(filename):
        print("\n", username,"\ndidn't generate recipies before, Do that:")
        username , done = generate_recipe_recommendations.generate_recipe_recommendations(username,False)
        done = done
        return username

    servings_num = int(input("Enter servings number per meal to perform the health analysis: "))
    recipes_list = read_recipes("recipes.csv")
    
    TEE = generate_recipe_recommendations.bring_TEE(username)

    user_gen_recipes_list = read_user_meals(filename)
    
    gen_recipes_names = []    
    meals_count_list = []
    for session in user_gen_recipes_list:
        session_meals_count = 0
        for meal in session[1]:
            gen_recipes_names.append(meal)
            session_meals_count += 1 
        meals_count_list.append(len(session[1]))        

    detailed_gen_recipes = []
    for line in recipes_list:
        for session in user_gen_recipes_list:
            if line[1] in session[1]:
                detailed_gen_recipes.append(line)
                meals_count_list.append(len(session[1]))                 
                
        
    calories_list = []
    recipes_num = 1
    total_cal = 0
    for recipe in detailed_gen_recipes:        
        display_recipe(recipe , recipes_num, servings_num) 
        index = detailed_gen_recipes.index(recipe)
        cal = float(recipe[9])
        total_cal += cal
        calories_list.append(cal* servings_num)
        if cal * servings_num > (TEE / meals_count_list[index])  :
            status = "caloric surplus"
        else:
            status = "caloric deficit"
        print("\nStatus : \n" , status )
        print("overall trend of the caloric status: ", )
        recipes_num += 1
    
    print("\nTotal calories per session : " , total_cal)
    print("\nAverage calories per session : " , total_cal / len(meals_count_list) )
    
    print("\nTotal calories : " , sum(calories_list))
    print("TEE = ", TEE)
    
    if sum(calories_list) > TEE:
        cal_state = "surplus"
    else:
        cal_state = "deficit"
    total_calories = str(sum(calories_list))
    avarage_cals = str(sum(calories_list)/len(meals_count_list))
    mealsCount = meals_count_list[0]
    print("Overall, "+ username + " shows that there is a calories "
        + cal_state +" in " + str(mealsCount) +  " meals calories from record # 1.")
    print("The total calories  in the meals is " + total_calories + " calories")
    print("calories The Average calories  of the meals is "+ avarage_cals +" calories")
    
    # plotting calories list
    plot_calories_list(calories_list,1)



    return username
