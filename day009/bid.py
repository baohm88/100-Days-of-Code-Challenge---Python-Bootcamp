bids = {}

bidding_finished = False

def find_highest_bid(bids):
  highest_bid = 0
  winner = ''
  for bidder in bids:
    bid_amount = bids[bidder]
    if highest_bid < bid_amount:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What's your name? ")
  amount = int(input("What's your bid? $"))
  bids[name] = amount
  should_continue = input("Are there any other bidders? ").lower()
  if should_continue == 'no':
    bidding_finished = True
    find_highest_bid(bids)
  else:
    bidding_finished = False