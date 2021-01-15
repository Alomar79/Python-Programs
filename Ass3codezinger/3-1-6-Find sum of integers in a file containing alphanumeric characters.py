# Write your code here...
x = input()
alist = []
while x != '$':
    alist.append(x)
    x = input()
alist.append(x)
S = ''
for x in alist:
    S += x + '\n'

outfile = open('file.txt','w')
outfile.write(S)
outfile.close()

sum = 0
infile = open('file.txt','r')
line = infile.readline()
while line != '':
    for ch in line:
        if ch.isnumeric():
            k = int(ch)
            sum += k
    line = infile.readline()
infile.close()    
print(sum)

