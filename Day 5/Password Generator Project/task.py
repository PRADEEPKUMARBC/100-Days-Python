import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# for i in range(1, nr_letters + 1):
#     random_letter = random.randint(0, nr_letters)
#     print(letters[random_letter], end="")
#
# for i in range(1, nr_symbols + 1):
#     random_symbol = random.randint(0, nr_symbols)
#     print(symbols[random_symbol], end="")
#
# for i in range(1, nr_numbers + 1):
#     random_number = random.randint(0, nr_numbers)
#     print(numbers[random_number], end="")


password_list = []

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print("".join(password_list))
random.shuffle(password_list)
print(password_list)

remake_password = ""
for char in password_list:
    remake_password = remake_password + char
print(remake_password)