ifile = open('test.txt', 'r')
lst = []
c = 0
for x in ifile:
    c += 1
    if c % 2 != 0:
        continue
    
    z = int(x)
    lst.append(z)
    

print(lst)

ifile.close()


