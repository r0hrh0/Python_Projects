import os

auction = {}


def add_bid(bidder_name, bidding_price):
    auction[bidder_name] = bidding_price
    return auction


continue_bid = True
auction_list = {}
while continue_bid:
    check = input("Are there any bidders? (y/n)").lower()
    if check == "y":
        os.system("cls")
        name = input("What is the bidder's name? : ")
        bid = int(input("How much is the bid? : "))
        os.system("cls")
        auction_list = add_bid(bidder_name=name, bidding_price=bid)
        winning_bid = 0
        winner = ""
        for bidders_name in auction_list:
            if auction_list[bidders_name] > winning_bid:
                winning_bid = auction_list[bidders_name]
                winner = bidders_name

    elif check == "n":
        if auction_list == {}:
            print("No bidders.")
        else:
            print(auction_list)
            print(f"The winning bid is {winning_bid} and the winner is {winner}.")
            continue_bid = False
