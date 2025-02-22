import art
print(art.logo)

def find_highest_bidder(bidding_dictionary):
    winner=''
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}
continue_bid = True
while continue_bid:
    name = input("What is your the name?: ")
    price = int(input("what is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any another bidders? 'yes' or 'no' \n".lower())
    print("\n"*100)
    if should_continue == 'no':
        continue_bid = False
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        continue_bid = True
        print("\n" * 20)