# Name : Noor AlNajjar
# QU ID: 201901316

def main():
    # ask user to enter the sentence to fix
    text = str(input("please enter a sentence so I can fix it: "))
    myList = []
    sentence = ''
    for ch in text:
        # check if the character (of the input string) is a number
        # then will change it to space
        if ch.isnumeric():
            ch = ' '
        ch = ch.lower()
        sentence += ch
    # convert the sentence into a List with words splited inside.
    myList = sentence.split(' ')

    # print the words from the list
    for word in myList:
        if myList.index(word) == 0:
            word = word.title()
        print(word + ' ' , end = '')
    print('\n')

# call main function
main()
            
