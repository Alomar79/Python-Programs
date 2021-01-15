# Student name:  Najla_Alkhater  -    QUID: 201409664

def main():
    sentence = str(input('Please Enter a Sentence so I can fix it: '))
    cleanedSentence = ''
    for char in sentence:  
        char = char.lower()    
        if char.isnumeric():
            char = ','        
        cleanedSentence = cleanedSentence + char

    words_list = cleanedSentence.split(',')
    print("The fixed string is: ", end ='')
    
    for word in words_list:
        # check if word at the first index
        if word == words_list[0]:
            word = word.title()
        if word == words_list[len(words_list)-2]:
            print(word  , end = '')
        else:
            print(word + ' ' , end = '')

# call main function
main()
