# Write your code here...
x = input()
alist = []
outfile = open("file.txt","w")
while x!= '$':
    alist.append(x)
    x = input()
alist.append(x)
x = input()
alist.append(x)
S = ''
for x in alist:
    S += x + '\n'
outfile.write(S)
outfile.close()

index = 1
str1 = ''
for x in alist:
    if alist.index(x) == index:
        continue
    if x == "$":
        str1 += x + '\n'
        break
    else:
        str1 += x + '\n'
#print(str1)
ofile = open("file.txt", "w")
ofile.write(str1)
ofile.close()

lines = []
infile = open("file.txt","r")
line = infile.readline().rstrip()
lines=[]
while line != '$':
    lines.append(line)
    line = infile.readline().rstrip()
lines[2] += ' '
lines[3] += ' '
for x in lines:
    if x != "$":
        print(x)
    #line = infile.readline().rstrip()
infile.close()