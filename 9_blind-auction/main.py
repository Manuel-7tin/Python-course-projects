from replit import clear
import art
# HINT: You can call clear() to clear the output in the console.

bids = {}


def decider(ps_name, ps_bid):
    bids[ps_name] = ps_bid

# Print app logo and welcome message
stion = True
print(art.logo)
print("Welcome to the secret auction program")
# Request bidders info and decisions until there are no bidders left
while stion == True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bidders = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    decider(name, bid)
    if bidders == "no":
        stion = False
    clear()

high_bid = 0
# Determine and declare winner
for name in bids:
    if high_bid < bids[name]:
        high_bid = bids[name]
for name in bids:
    if high_bid == bids[name]:
        print(f"The winner is {name} with a bid of ${high_bid}")
