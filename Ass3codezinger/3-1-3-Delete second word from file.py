import os, errno
def solution(FN):
    # Write your code here
    inputfile = open(FN , "r")
    line = inputfile.readline().rstrip()
    mylist = line.split(' ')
    del mylist[1]
    while line != '':
        line = inputfile.readline().rstrip()
        mylist.append('\n' + line)
    inputfile.close()
    outfile = open(FN , "w")
    str1 = ''
    for x in mylist:
        str1 += x + ' '
    outfile.write(str1)
    outfile.close()
    
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
        break
    else:
        break
S = '\n'.join(lines)
f1 = open("story.txt","w")
f1.write(S)
f1.close()
solution("story.txt")
f1 = open("story.txt","r")
print(f1.read(),end='')
f1.close()
try:
    os.remove("story.txt")
except OSError:
    pass