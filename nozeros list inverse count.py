"""
Write a while loop that filters all non-zero numbers from a given list and places them in a new list, called nozeros. Your code should also output the number of zeros found in the list. For example, given the list nums = [2, 5, 0, 4, 3, 0, 10, 0, 8, 8, 20], your program output should be:

nozeros=  [20, 8, 8, 10, 3, 4, 5, 2]
total zero entries = 3
"""

## solution 
nums = [2, 5, 0, 4, 3, 0, 10, 0, 8, 8, 20]

nozeros = [ ]

nums.reverse()
for f in nums:
    if f ==0:
        continue
    nozeros.append(f)


zeros=nums.count(0)





    
print('nozeros= ',nozeros)
print('total zero entries =', zeros)