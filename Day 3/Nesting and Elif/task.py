print("Welcome the rollercoaster!")
height = int(input("Enter your height: "))
bill = 0

if height > 120:
    age = int(input("Enter your age: "))
    if age <= 12:
        bill = 5
        print("You Pay $5")
    elif age <= 18:
        bill = 7
        print("You Pay $7")
    else:
        bill = 10
        print("You Pay $10")
    want_photos = input("Do you want to take a photo ? y for yes and n for no: ")
    if want_photos == "y":
        bill += 3
        print(f"You Rolled {bill}")

else:
    print("You have to grow the taller before you can ride the rollercoaster")