def solution(S):
    # Write your code here...
    expr = []
    for ch in S:
        if ch in ['(' , '{' , '[']:
            expr.append(ch)
        else:
            if not expr:
                return 'No'
            sChar = expr.pop()
            if sChar == '(':
                if ch != ')':
                    return 'No'
            if sChar == '{':
                if ch != '}':
                    return 'No'
            if sChar == '[':
                if ch != ']':
                    return 'No'
    # check if still chars in the list            
    if expr:
        return 'No'
    return 'Yes'
                  
                    
# S = "[()]{}{[()()]()}"
S = input()
print(solution(S),end='')