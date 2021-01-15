import os
# import edit_or_delete_userprofile
import create_load_profile
import generate_recipe_recommendations


def read_gen_user_recipes(filename):    
    infile = open(filename,'r')
    next(infile)
    user_generated_recipes = []
    line = infile.readline().rstrip()
    while line != '':
        line_lst = line.strip().split(';')
        user_generated_recipes.append(line_lst)        
        line = infile.readline().rstrip()
    infile.close()
    return user_generated_recipes

def read_recipes(CSV_FILENAME):    
    infile = open(CSV_FILENAME,'r')
    next(infile)
    recipes_list = []
    line = infile.readline().rstrip()
    while line != '':
        line_list = line.strip().split(';')
        recipes_list.append(line_list)
        line = infile.readline().rstrip()
    infile.close()
    return recipes_list

def display_recipe(recipe, order_no , servings_size): 
    # make a list from ingredients, which is at index 7 in recipe.csv
    lst = list(recipe[7].strip().split(","))
    Ingredients = ""
    for n in lst:
        if n != " ":
            Ingredients += "- " + n + "\n"
    print("\nGenerated Recipe #" , order_no)
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
        print("\nimage : ",  generate_recipe_recommendations.showImage2(recipe[11]))
        print("\nIngredients : \n", Ingredients ) #recipe[7]
        print("\nDirections.. : \n", recipe[8] )

def plot_calories_list(calories_list , session_number):
    import matplotlib.pyplot as plt

    slice_labels = []
    lst = list(range(len(calories_list)))
    for i in lst:
        slice_labels.append("Meal #"+str(i+1))
    
    sum_cal = str(round(sum(calories_list),2))
    plt.title("Calorie distribution of the meals" \
        +" from session # "+str(session_number)+" \n(total is: "+ sum_cal +" calories)")
    plt.pie(calories_list , labels=slice_labels, autopct='%1.2f%%')
    plt.show()

#function that uses the randomly generated recipe names of the user 
# to search for their details from the file recipes.csv. 
# The function return the details of all the randomly generated recipes by the user
def get_detailed_gen_recipes(gen_user_recipes , recipes_list):
    gen_user_recipes_names = []
    names_count = 0
    for line in gen_user_recipes:
        names = line[1]
        names_list = names.strip().split(',')
        for name in names_list:
            gen_user_recipes_names.append(name.strip())
            names_count += 1
    
    detailed_gen_recipes = []
    for name in gen_user_recipes_names:
        found = True
        for line in recipes_list:
            if name == line[1] and found == True:
                detailed_gen_recipes.append(line)
                found = False  
    return detailed_gen_recipes

def view_usermeals_health_info(username):
    if username == "stranger":
        print("No username under the name: " , username)
        username= create_load_profile.create_load_profile(username)
        return username
    
    filename = str(username) + "-recipes.txt"
    if not os.path.exists(filename):
        print("\n[" , username , "] Generated recipies not found , generate now")
        username, done =generate_recipe_recommendations.generate_recipe_recommendations(username,False)
        done = done
        return username
    # Read all generate recipes for the user
    gen_user_recipes = read_gen_user_recipes(filename)
    servings_num = int(input("Enter servings number per meal to perform the health analysis: "))
    TEE = generate_recipe_recommendations.get_TEE(username)
    # bring all lines in recipes
    recipes_list = read_recipes("recipes.csv")
    # save all recipes names founded in username-recipe.txt to a list    

    detailed_gen_recipes = get_detailed_gen_recipes(gen_user_recipes , recipes_list) 

    names_count_list = []
    names_count = 0
    for line in gen_user_recipes:
        names = line[1]
        names_list = names.split(',')
        for name in names_list:
            names_count += 1
            name = name
        names_count_list.append(str(names_count))
        names_count = 0
    
    calories_list = []
    order_no = 1
    total_cal = 0
    myList = detailed_gen_recipes
    for k in range(len(names_count_list)):
        namesCount = int(names_count_list[k])
        for i in range(namesCount):
            i = i
            recipe = myList[0]
            cal = float(recipe[9])
            myList.remove(recipe)
            total_cal += cal
            calories_list.append(cal* servings_num)
            display_recipe(recipe , order_no, servings_num) 
            
            if cal * servings_num > (TEE / namesCount):
                status = "caloric surplus"
            else:
                status = "caloric deficit"
            print("\nStatus : \n" , status )
            print("\noverall trend of the caloric status: ", )
            order_no += 1

        average_cal = total_cal / namesCount

        print("\nTotal calories per session : " , total_cal)
        print("\nAverage calories per session : " , average_cal )
        total_cal = 0
    
    """print("\nTotal calories : " , sum(calories_list)/servings_num)
    print("TEE = ", TEE)"""

    if sum(calories_list) > TEE:
        cal_state = "surplus"
    else:
        cal_state = "deficit"
    print("Overall, "+ username + " shows that there is a calories "
        + cal_state +" in " + str(namesCount) +  " meals calories from record # 1.")
    print("The total calories  in the meals is " + str(sum(calories_list)/servings_num) + " calories")
    print("calories The Average calories  of the meals is "+ str(average_cal) +" calories")
    
    plot_calories_list(calories_list,1)

    return username
