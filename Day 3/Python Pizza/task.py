print("Welcome to Python Pizza Deliveries!")
pizza_size = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want to pepperoni on pizza? (y/n): ")
extra_chees = input("Do you want extra chees? (y/n): ")

bill = 0

# todo : How much they need to pay on their size
if pizza_size == "S":
    bill += 15
elif pizza_size == "M":
    bill += 20
elif pizza_size == "L":
    bill += 25

# todo:  work out how much to add their bill based on their pepperoni choice
if pepperoni == "Y":
    if pizza_size == "S":
        bill += 2
    else:
        bill += 3

# todo: work out their final amount based on whether if they want extra cheese

if extra_chees == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")



