import sys

def solution(A1, A2):
    # Write your code here.
    for i in range(len(A1)):
        for j in range(len(A1[0])):
            A1[i][j] = A1[i][j] + A2[i][j]
    return A1
def createMatrix(M,N):
    A = []
    for n in range(M):
       R = [int(e) for e in input().split()]
       assert(len(R) == N)
       A.append(R)
    return A

M = int(input())
N = int(input())
A1 = createMatrix(M,N)
A2 = createMatrix(M,N)
Res = solution(A1, A2)
count=0
for l in Res:
    count+=1
    i=1
    for num in l:
        if i == N:
            print(num, end='', flush=True)
        else:
            print(num, sep=' ', end=' ', flush=True)
        i+=1
    if count < len(Res):
        print("\n",end='')