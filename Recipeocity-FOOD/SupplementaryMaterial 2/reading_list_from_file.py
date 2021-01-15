#This example shows you how to read a list from a csv file
FOOD = 'indian_food.csv' #Declare the file name as constant

#This boolean function searches for a string in a list
def list_search(ingredient,ingredientsList):
    found = False
    if ingredient in ingredientsList:
        found = True
    else:
        found = False
    return found

def main():
    food_file = open(FOOD,'r') #Open the food file in read mode
    next(food_file) #This statement will skip the first line (header) in the CSV file
    
    for line in food_file:
        foodData = line.strip().split(';')
        dishName = foodData[0] #Name of dish or recipe
        ingredients = foodData[1] #Ingredients of the recipe
        #The ingredients here are comma separated, so, we can convert them to a list
        ingredientsList = ingredients.replace(' ','').split(',')#Remove white space before splitting string to list
        #Remove the comment from the next line to see the list that you just created
        #print(ingredientsList)

        #How about we search inside the list for a specific ingredient?
        #Call a function called listSearch and pass the ingredientsList as parameter.
        #Let's search for recipes with banana in them:
        if list_search('banana',ingredientsList):
            print(dishName)
            print(ingredients)
main()