"""
Write a Python program that computes the following sum

∑1/𝑥,  ∀𝑥∈{2,5,0,4,3,0,10,0,8,8,20}
𝑥≠0 

a) using a while loop

b) using a for loop

Round your results to three decimal places.

"""

nums = [2,5,0,4,3,0,10,0,8,8,20]

y= 0

while nums:    
    r = nums.pop()
    if r == 0:
        continue
    y += 1 / r
    

print('sum = ',format(y, '0.3f'))


"""
by for loop:
nums = [2,5,0,4,3,0,10,0,8,8,20]

sum= 0

for r in nums:    
    
    if r != 0:
        sum += 1 / r
    

print('sum = ',format(sum , '0.3f'))
"""