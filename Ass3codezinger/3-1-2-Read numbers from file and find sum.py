# Write your code here...
try:
    outfile = open("file.txt","a")
    inp = input()
    while inp != '$':
        inp = int(inp)
        outfile.write(str(inp) + "\n" )
        inp = input()

    if inp == '$':
        outfile.write(inp)
    outfile.close()
except IOError:
    print("IO Exception")
try:
    sum = 0
    inputfile = open("file.txt","r")
    line = inputfile.readline().rstrip()
    while line != '$':
        line = int(line)
        sum += line
        line = inputfile.readline().rstrip()
    inputfile.close()
except IOError:
    print("Input IO Exception")
print(sum)