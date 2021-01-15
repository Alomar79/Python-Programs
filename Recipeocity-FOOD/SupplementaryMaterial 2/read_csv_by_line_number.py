#This example shows you how to read a csv file by line number
FOOD = 'indian_food.csv' #Declare the file name as constant

def main():
    food_file = open(FOOD,'r') #Open the food file in read mode
    next(food_file) #This statement will skip the first line (header) in the CSV file
    foodList = food_file.readlines() #This allows you to read all lines from a file into a list.
    
    #Now you can read a specific line from the file, for example if we want to read line 5 (open the file indian_food.csv and look at line 5)
    myFavoriteRecipe = foodList[4] #Gulab jamun recipe
   
    #We can also extract information from this file as follows:
    foodData = myFavoriteRecipe.strip().split(';')
    dishName = foodData[0] #Name of dish or recipe
    ingredients = foodData[1] #Ingredients of the recipe
    diet = foodData[2] #The dish type (i.e., is it vegetarian or contains meat?)
    print("Recipe Name:",dishName)
    print("Ingredients:")
    #Convert ingredients to list and print them line by line
    ingredientsList = ingredients.replace(' ','').split(',')#Remove white space before splitting string to list
    counter = 0 #Create a counter for ingredients list
    for item in ingredientsList:
        counter+=1
        print(str(counter)+'-'+item) #Printing each ingredient
    print("Diet:",diet)
                
main()