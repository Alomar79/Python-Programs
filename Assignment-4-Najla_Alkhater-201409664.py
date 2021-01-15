
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

    print ("\nThe average price of iPhones is : $" , format(average,"0.2f") , "\n")

def main():
    # calling function iphone_statistics(file_name)
    iphone_statistics("iphones.txt")

main()