#This example shows you how write a list to a file
FOOD = 'indian_food.csv' #Declare the file name as constant
RESULT = 'my_recipes.csv' #Declare the file name that you want to write as constant

def read_file(indian_food):
    myRecipesList = []
    food_file = open(indian_food,'r') #Open the food file in read mode
    header = next(food_file) #This statement will skip the first line (header) in the CSV file
    for line in food_file:
        foodData = line.strip().split(';')
        cook_time = foodData[4] #Recipe cooking time
        region = foodData[8] #From which region does this recipe come from in India? East, West, North, South?
        
        #I am interested in recipes from west india that can be cooked in less than 30 minutes
        if region.lower() == 'west' and int(cook_time) < 30:
            myRecipes = line.strip()
            #print(myRecipes) #For testing, un-comment this to see the result
            myRecipesList.append(myRecipes) #Add my recipes to a list
    return header, myRecipesList #Return the header to write it to the file
    
def write_file(header,theRecipes,resultsFile):
    results_file = open(resultsFile,'w') #Change to w if you want to append
    #Iterate over the list and write it to the file
    results_file.write(header)#This will write a header to the file (column names)
    for item in theRecipes:
        results_file.write(item+'\n')
    print("Done writing my favorite recipes to the file my_recipes.csv")

def main():
    columns, myRecipes = read_file(FOOD)
    write_file(columns,myRecipes,RESULT)

main()


