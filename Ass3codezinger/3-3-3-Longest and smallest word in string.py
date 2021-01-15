# Write your code here...
S = input()
lst = S.split(' ')
maxword = ''
minword = lst[0]
for word in lst:
    if len(word) > len (maxword):
        maxword = word
    if len(word) < len ( minword):
        minword = word
print( maxword)
print( minword)