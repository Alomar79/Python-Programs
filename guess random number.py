import  random
number = random.randint(1, 20)

def rand_call(guess ):
    #global number
    if guess < number:
        print("Your guess number is low")
    elif guess > number:
        print("Your guess number is high") 

def main():
    guesses_no = 1 
    print("Type a number betwen 1 and 20: ")
    while guesses_no < 6:
        user_guess=int(input("What is your guess mate?\n")) 
        guesses_no = guesses_no + 1         
        rand_call(user_guess)
        if user_guess == number:
            break
        
    if user_guess == number:
        print("The random number was",number,"and your guess was correct ")
        print("The  number of guesses you took is",guesses_no - 1) 
    else:
        print("The random number was",number,"and your guess was incorrect ")

main()