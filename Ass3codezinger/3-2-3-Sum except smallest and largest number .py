
def solution(L):
    # Write your code here.
    nums = []
    for x in L:
        x = int(x)
        nums.append(x)
    nums.remove(max(nums))
    nums.remove(min(nums))
    total = sum(nums)
    return total
        
N=int(input())
L=[]
n=0
for e in input().split():
    if(n<N):
        L.append(int (e))
        n+=1
if(n<N):
    print("Please input {0} elements".format(N),end='')
else:
    print(solution(L),end='')