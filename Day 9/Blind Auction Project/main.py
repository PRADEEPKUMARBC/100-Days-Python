import art
print(art.logo)

def find_highest_bidders(bidder_record):
    highest_bid = 0
    winner = ""
    for bidder in bidder_record:
        bid_amount = bidder_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with a bid of ${highest_bid} ")

bids = {}
continue_bidding = True
while True:
    name = input("What is your name? ")
    price = float(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Is there any other bidders? (Y/N) ? Type 'Yes' or 'no  ")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidders(bids)
    elif should_continue == "Yes":
        print('\n' * 20)
