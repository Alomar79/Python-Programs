# Write your code here...
import math
x = input()
alist = []
while x != '$':
    x = int(x)
    alist.append(x)
    x = input()
alist.append(x)
#print(alist)
S = ''
for x in alist:
    S += str(x) + '\n'
ofile = open('file.txt','w')
ofile.write(S)
ofile.close()
#print(S)
primes = []

infile = open('file.txt','r')
line = infile.readline().rstrip()

"""
if line != "$":
    g = int(line)
    print(math.ceil(math.sqrt(g)))
#print(line)

"""
p = False
#line = line.strip()
#alist.pop()
while line != '': 
    if line == '$':
        break
    num = int(line)
    #print(num/2)
    #sq = math.sqrt(num)
    #y = math.ceil(sq)
    #print(sq , "\n")
    for i in range(2 , 100):
        if num % i == 0:
            p = False
            break
        else:
            p = True
    if p == True:
        primes.append(num)
        p == False
    line = infile.readline().rstrip()
    
infile.close()
# print(primes)

primeFile = open('prime.txt','w')
str1 =''
for x in primes:
    str1 += str(x) + '\n'
primeFile.write(str1)
primeFile.close()
# Display content
ifile = open('prime.txt','r')
line = ifile.readline().rstrip()
while line != '':
    print(line)
    line = ifile.readline().rstrip()
ifile.close()
