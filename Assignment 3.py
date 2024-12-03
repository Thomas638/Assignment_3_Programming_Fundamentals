# I Thomas Carroll, 000841321, certify that this work is my own effort and that I have not allowed anyone else to copy from it.
# MyCanvaswould not accept .py file extensions, this is why I have change the file type to .txt

import random

# Function ====================================================================================================================

def checkGuess():
    #userGuess = int(userGuess)
    if userGuess == secretNumber:
        return 0

    elif userGuess < secretNumber:
        return -1

    else: userGuess > secretNumber
    return 1




''' Test Section
userName = Tim Nice But Dim
userGuess = 3
secretNumber = 2

result = checkGuess()
print(result)
'''

# Main Code ====================================================================================================================

userName = input("Enter user name: ")
score = 0
secretNumber = len(userName) * random.randint(1,5)
guesses = 0
print("Hello", userName, "welcome to the guessing game!")

remaining = 3
while remaining  > 0:
    remaining = 3 - guesses
    #print(remaining, " guesses left!")
    if remaining > 1:
        print(remaining, " guesses left!")

    else:
        print("You have 1 guess left!")

    userGuess = int(input("What is your Guess? "))
    guesses = guesses + 1
    result = checkGuess()
    if result == 0:
        if guesses == 1:
            print("Amazing! On your first guess!")
            score = score + 10
            remaining = 0

        else: 
            if guesses == 2:
                print("Exellent! On your second guess!")
                score = score + 5
                remaining = 0

            else:
                print("Lucky! On your last guess!")
                score = score + 1           
                remaining = 0
    else:
        if result == -1:
            print("Your guess of ", userGuess, " was too low!")
            remaining = remaining -1

        else:
            print("Your guess of ", userGuess, " was too high!")
            remaining = remaining -1

print("Thank you for playing", userName, ", your score was: ", score, " points!" " The secret number was: ", secretNumber)