#This example shows you how to read a csv file
FOOD = 'indian_food.csv' #Declare the file name as constant

def main():
    food_file = open(FOOD,'r') #Open the food file in read mode
    next(food_file) #This statement will skip the first line (header) in the CSV file
    sweetCounter = 0 #Initialize a counter to count sweets
    for line in food_file:
        foodData = line.strip().split(';')
        dishName = foodData[0] #Name of dish or recipe
        ingredients = foodData[1] #Ingredients of the recipe
        diet = foodData[2] #The dish type (i.e., is it vegetarian or contains meat?)
        prep_time = foodData[3] #Recipe preparation time
        cook_time = foodData[4] #Recipe cooking time
        flavor = foodData[5] #Is the food sweet or savory or other?
        course = foodData[6] #What type of dish is this? Main course, desert?
        state = foodData[7] #From which state does this recipe come from in India?
        region = foodData[8] #From which region does this recipe come from in India? East, West, North, South?
        
        #Let's try printing recipes from east India
        if region.lower() == 'east':
            print(line.strip())
        #How about counting how many dishes are sweet?
        if flavor.lower() == 'sweet':
            sweetCounter+=1
    
    print("The total number of sweet dishes is:",sweetCounter)
            
main()