print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give 12 10 or 18 ?"))
split_bill = int(input("How many people to split the bill?"))

amount = ((bill * ( tip / 100)  + bill ) / split_bill)
final_amount = round(amount, 2)
print(f"Each Person should pay: {final_amount}$")