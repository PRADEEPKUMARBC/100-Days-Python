from random import randint
from art import logo

print(logo)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, actual_answer, turns):
    """ Checks answer against guess, returns the number of turns"""
    if user_guess > actual_answer:
        print("Too High")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You guessed correctly! the actual answer is : {actual_answer}")

# Function to set difficulty
def set_difficulty():
    level = input("Choose difficulty. Type 'easy' or 'hard' : ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# Function to check user's guess against actual answer
def game():
    # choosing a random Number between 1 to 100
    print("Welcome to the number guessing game! ")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Psst, the correct answer is : {answer}")

    turns = set_difficulty()

    # Let the user guess a number
    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number")
        # Let user Guess the number
        guess = int(input("Make a Guess : "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses, you loose. ")
            return
        elif guess != answer:
            print("Guess Again.")

game()

    # Track the number of turns and reduce by 1 if they get it wrong


    # Repeat the guessing functionality if they get it wrong
