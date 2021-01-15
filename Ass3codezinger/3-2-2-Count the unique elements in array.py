# Write your code here...
length = input()
alist = input().split(' ')
counter = 0
for x in alist:    
    if alist.count(x) == 1:
        counter = counter + 1
print(counter)
    