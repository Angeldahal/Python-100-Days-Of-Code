from art import logo
import os

def clear():
    os.system( 'clear' )

print(logo)
other_bidders = True
bids = {}
while other_bidders:
    bidder_name = input("What is your name?\t")
    bid_amount = int(input("Enter the bid amount:\t"))
    check_other_bidders = input("Type yes if there are other biddeers and no if there are none\t")
    if check_other_bidders == 'no':
        other_bidders = False
    clear()
    bids[bidder_name] = bid_amount
def highest_bidder(bidding_record):
    greatest_bidder = ""
    greatest_bid = 0
    for i in bidding_record:
        if bidding_record[i] > greatest_bid:
            greatest_bidder = i
            greatest_bid = bidding_record[i]
    print(f"The winner is {greatest_bidder} with a bid of {greatest_bid}.")

highest_bidder(bids)