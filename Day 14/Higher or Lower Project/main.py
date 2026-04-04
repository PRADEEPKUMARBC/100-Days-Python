# Design Part
from art import logo
from game_data import data
import random

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr} , from {account_country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

# Generate the account in random
account_b = random.choice(data)
game_should_continue = True
while game_should_continue:

    account_a = account_b:
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)q

    print(f"Compare A : {format_data(account_a)}")
    print(f"Compare B : {format_data(account_b)}")

    guess = input("Who has more followers ? Type 'A' or 'B': ").lower()

    guess = input("Who has more followers? Type 'A' or 'B' : ").lower()

    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_followers_count, b_followers_count)

    score = 0
    if is_correct:
        score += 1
        print(f"Correct! You got it in {score} guesses!")
    else:
        print(f"Wrong! You got it in {score} guesses!")
        game_should_continue = False