def solution(N, A):
    # Write your code here...
    return max(A)+ min(A)


N = int(input())
A = []
n = 0
for e in input().split():
    if(n<N):
        A.append(int(e))
        n+=1

print(solution(N, A))