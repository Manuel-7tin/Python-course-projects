# Print welcome message
print("Welcome to the University of Lagos")
# Get user's mode of transportation
choice = input('You are at the main gate. What do you want to do? Type "trek" or "cab"\n').lower()
# Get  user's decisions and decide their fate
if choice == "trek":
    action = input(
        'You come to a cluster of lecture halls. There is a fight scene outside. Type "ignore" to enter a hall. Type "watch" to watch the fight.\n').lower()
    if action == "ignore":
        decision = input(
            "You arrive at the lecture halls unharmed. There are 3 halls. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if decision == "red":
            print("You enter a hall of eternal exams. Game Over!")
        elif decision == "yellow":
            print("You enter a hall with a Billion dollar Treasure. YOU WIN!")
        else:
            print("You enter a hall of hyenas. Game Over!")
    else:
        print("You watched till the halls closed. Game over!")
else:
    print("You drove into a gutterr, game over!")
