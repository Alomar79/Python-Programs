"""Write a new function rzeros that removes the zeros from any given list of numbers, and returns a list with all zeros removed as well the number of zero entries in the list and non-zero entries in the list. The returned list preserves the original order of the non-zero numbers.

For example, given the list numlist = [2, -4, 0, 0, -1, 5, 2, -4, 0, -2, 7, -1], your function should return the tuple

([2, -4, -1, 5, 2, -4, -2, 7, -1], 9, 3)

"""

def rzeros(nums):
    """remove zeros from input list nums and returns a list"""
    total = len(nums)
    zeros = 0
    nozeros = []
    for x in nums:
        if x != 0:
            nozeros.append(x)        
        else:
            zeros = zeros + 1
            
    return (nozeros, total - zeros, zeros) 
    
numList = [2, -4, 0, 0, -1, 5, 2, -4, 0, -2, 7, -1]
print()
print(rzeros(numList))
