
def solution(S):
    #write your code here
    counter = 0
    myList = []
    
    for x in S:
        if S.isalpha:
            myList.append(x)
    for ch in myList:
        if myList.count(ch) > 1:
            counter += 1
            for y in myList:
                if y == ch:
                    myList.remove(y)
    return counter
        
S = input()
print(solution(S),end='')