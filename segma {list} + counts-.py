"""
∑1/𝑥,  ∀𝑥∈{2,5,0,4,3,0,10,0,8,8,20}
𝑥≠0

Modify your code for the above problem to calculate the sum of reciprocals as well as the number of non-zero entries included in the sum calculation. For the given list nums = [2, 5, 0, 4, 3, 0, 10, 0, 8, 8, 20] your output should be:

sum =  1.683
total zero entries = 3
total non-zero entries = 8

"""

nums = [2,5,0,4,3,0,10,0,8,8,20]

sum = 0
count = 0
totalLength = len(nums)
while nums:    
    r = nums.pop() 
    if r != 0:
        sum += 1 / r
    else:    
        count += 1    

print('sum = ',format(sum , '0.3f'))
print('total zero entries = ', count)
print('total non-zero entries = ', totalLength - count)


