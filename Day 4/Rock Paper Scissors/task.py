rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

rps_list = [rock, paper, scissors]
user_choice = int(input("Select Rock or Paper or Scissors 0 for Rock , 1 for Paper , 2 for Scissors : "))
print(rps_list[user_choice])

computer_decision = random.randint(0, 2)
print("computer Chooses")
print(rps_list[computer_decision])

if user_choice == 0 and computer_decision == 1:
    print("computer win!")
elif user_choice == 0 and computer_decision == 2:
    print("computer win!")
elif user_choice == 1 and computer_decision == 0 :
    print("User Win!")
elif user_choice == 1 and computer_decision == 2:
    print("computer win!")
elif user_choice == 2 and computer_decision == 0:
    print("Rock win!")
elif user_choice == 2 and computer_decision == 1:
    print("User Win!")
elif user_choice == computer_decision:
    print("Draw")
else:
    print("Invalid Try Again!")

