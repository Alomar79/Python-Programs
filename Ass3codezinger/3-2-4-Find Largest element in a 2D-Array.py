
def solution(L):
    # Write your code here.
    Max = 0
    rows = len(L)
    cols = len(L[0])
    for m in range(rows):
        for n in range(cols):
            if L[m][n] > Max:
                Max = L[m][n]
    return Max
    
L = []
M = int(input())
N = int(input())
n=0
for n in range(M):
    R = [int(e) for e in input().split()]
    assert(len(R) == N)
    L.append(R)

print(solution(L),end='')