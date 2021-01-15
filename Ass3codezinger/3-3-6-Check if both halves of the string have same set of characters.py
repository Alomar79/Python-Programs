# Write your code here...
S = input()
lst = []
for i in S:
    lst.append(i)
x = len(lst)
y = int(len(lst)/2)

if x % 2 != 0:
    lst.pop(y)

list1 = lst[0:y]
list2 = lst[y:]
for i in list1:
    if list1.count(i) == list2.count(i):
        F = True
    else:
        F = False
        break
if F == False:
    print("No")
else:
    print("Yes")

