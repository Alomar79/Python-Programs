# Write your code here...
import math

n = input()
arr = input().split(' ')
intArray = []
for i in arr:
    i = int(i)
    intArray.append(i)
myArr = []
for x in intArray:
    y = math.sqrt(x)
    if y in intArray:
        myArr.append(x)
print(sum(myArr))

        
