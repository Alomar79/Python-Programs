
def main():
    # receive the sentence to fix
    text = str(input("please enter a sentence so I can fix it: "))
    str1 = ''
    for ch in text:      
        if ch.isnumeric():
            ch = ' '
        ch = ch.lower()
        str1 = str1 + ch
    theList = str1.split(' ')

    for word in theList:
        # check if the is the first word in the list
        if theList.index(word) == 0:
            word = word.title()
        if word == theList[-2] and theList[-1]=='?':
            print(word  , end = '')
        else:
            print(word + ' ' , end = '')
    print('\n')

# call the main function
main()
            
