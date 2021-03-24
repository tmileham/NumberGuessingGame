# Number guessing game
########################
# Practising Python Functions - Tom M
########################
# 22-03-2021
########################
import random

# assign variables
guess_list = []
current_guesses = 0
guess_limit = 5

# Check the guess to see if its correct
def check_guess(value):
        if value < randomnumber:
            print("\t\nWrong, too low. Try again")
            guess_list.append(value)
            return False
        elif value > randomnumber:
            print("\t\nWrong, too high. Try again")
            guess_list.append(value)
            return False
        else:
            print("\t\nYou guess the correct number! Great work!")
            guess_list.append(value)
            if len(guess_list) == 1:
                print("\tWow first try, amazing work!")
            else:
                print(f" \nYou got it in {current_guesses+1} attempts, below were your guesses:")
                for guess in guess_list:
                    print(f"\t{guess}")              
            return True


# Function for user guess input
def input_guess():
    while True:
        try:
            guess =  int(input("\nPlease enter your guess: "))
        except ValueError:
            print("Invalid input - Please enter a number..")
            continue
        else:
            break
    return guess


# Function to allow user to set the guessing range
def define_range():
    while True:
        try:
            value = int(input("Define the upper limit of the random number: "))
        except ValueError:
            print("Invalid input - Please enter a number..")
            continue
        else:
            break   
    return value

upper_range = define_range()
randomnumber = random.randint(1,upper_range)

print(f"Okay you have {guess_limit} attempts at guessing a number between 1 and {upper_range}\nGood luck!")


#This is the main application loop, this only stops if the player wins/loses the game.
while current_guesses <= guess_limit:
    if current_guesses > 0:
        print(f"\tTotal guesses {current_guesses} \\ {guess_limit}\n\n======================================")
    if current_guesses == guess_limit:
        print("\nGame over, better luck next time!")
        break
    if check_guess(input_guess()):
        break
    current_guesses += 1



