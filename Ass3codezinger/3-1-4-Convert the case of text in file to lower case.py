# Write your code here...
x = input()
S = ''
outputfile = open("file.txt","w")
while x != "$":
    S = S + x + "\n"
    x = input()
S += "$"
outputfile.write(S)
outputfile.close()

S = S.lower()

ofile = open("file.txt","w")
ofile.write(S)
ofile.close()

infile = open("file.txt","r")
line = infile.readline().rstrip()
while line != "$":
    print(line)
    line = infile.readline().rstrip()
#print(line)
infile.close()

import os
os.remove("file.txt")