"""
A user wants to purchase an iPhone at an affordable price, so he collected the names and prices of used iPhone 11 devices and stored them in the file iphones.txt.
The file contains records with the following format: 
model(string)\nprice (float)

Help the user get some statistics about the iPhone records by reading the file ‘iphones’ and performing the following tasks:
•	Create a function called iphone_statistics(file_name) that prints the records of the iPhone with the following criteria:
o	The total number of records in the file.
o	The most expensive iPhone name and price.
o	The cheapest iPhone name and price (hint: initialize the cheapest price to 2000).
o	The average price of all iPhones in the file.
•	Create a main function that calls the function iphone_statistics and passes the file name ‘iphones.txt’ as argument to it.


"""



# Najla Alkhater 201409664

def iphone_statistics(file_name):
    bigPrice = 0.0
    cheapestPrice = 2000.0
    sumOfPrices = 0
    allRecords = 0
    inputFile = open("iphones.txt", "r")
    model = (inputFile.readline()).rstrip()
    line = (inputFile.readline()).rstrip()    
    while line != '':
        price = float(line)
        if price > bigPrice:
            bigPrice = price
            bigPrice_model = model
        elif price < cheapestPrice:
            cheapestPrice = price
            lowPrice_model = model
        allRecords += 1
        model = (inputFile.readline()).rstrip()
        line = (inputFile.readline()).rstrip()
        sumOfPrices += price 
        
    print("\nTotal number of records in the file:", format(allRecords ,'.0f'))
    print("The most expensive iphone has the following information: ")
    print("Model name: ", bigPrice_model)
    print ("iphone price: $" , bigPrice )
    
    print("\nThe cheapest iPhone has the following information: ")
    print("Model name: ", lowPrice_model)
    print ("iphone price: $", cheapestPrice)

    average = sumOfPrices / (allRecords )

    print ("\nThe average price of iPhones is : " , format(average,"0.2f") , "\n")


iphone_statistics("iphones.txt")