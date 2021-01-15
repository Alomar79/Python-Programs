"""
Solved Example: Given the list nums = [2, 5, 0, 4, 3, 0, 10, 0, 8, 8, 20], Write a while loop that prints all non-zero numbers from a list of numbers. The numbers should be printed in the same relative order they appear in the list.
"""

### using a while loop - solution 2
nums = [2, 5, 0, 4, 3, 0, 10, 0, 8, 8, 20]

nums.reverse()
while nums:     # while list nums is not empty pop only in while loop
    r = nums.pop()
    if r != 0:
        print(r)
    
    
print('done')