inputFile = open("Temprature.txt", "r")
sum = 0
count = 0
temp_list = []
line = (inputFile.readline()).rstrip()    
while line != '':
    temp = int(line)
    temp_list.append(temp)
    line = (inputFile.readline()).rstrip()
    sum += temp
    count += 1
print("The average annual change in temprature during the time period: \n")
print (sum / count)
print("\n\n")
print ("The greatest temperature degree during  the time period : \n")
print (max(temp_list))
print("\n\n")

print ("The smallest temperature degree during  the time period : \n")
print (min(temp_list))
print("\n\n")

five_years_list = temp_list[15:]
# print (five_years_list)

import numpy as np
import matplotlib.pylab as plt

x = np.arange(2016, 2020, 5)
y = np.arange(0, 20, 2.5)

plt.plot(y , x)

plt.xlim(2016, 2020)
plt.ylim(0, 20)

plt.xlabel('Year')
plt.ylabel('Tempratures')
#plt.grid( )

plt.show()