def solution(S1,S2):
    # Write your code here...
    r = 0
    S1 = S1.split(' ')
    S2 = S2.split(' ')
    str1 = ''
    str2 = ''
    for i in S1:
        str1 += i.strip().lower()
    for j in S2:
        str2 += j.strip().lower()
    for x in str1:
        if str1.count(x) == str2.count(x):
            r = 1
        else:
            r = 0
            break
    return r
    
S1 = input()
S2 = input()
print(solution(S1,S2),end='')