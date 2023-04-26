# Generate ascii art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# import module
import random
# Request users choice
ur_move = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors.\n"))
options = [rock, paper, scissors]
ur_choice = options[ur_move]
# Display ascii arts and determine computer choice
print(ur_choice)
pc_move = random.randint(0, 2)
pc_choice = options[pc_move]
print(f"Computer chose: {pc_choice}")
# Determine winner and inform user
if pc_choice == rock and ur_choice == scissors:
    print("You lose!")
elif pc_choice == rock and ur_choice == paper:
    print("You win!")
elif pc_choice == scissors and ur_choice == rock:
    print("You win")
elif pc_choice == scissors and ur_choice == paper:
    print("You lose")
elif pc_choice == paper and ur_choice == scissors:
    print("You win")
elif pc_choice == paper and ur_choice == rock:
    print("You lose")
elif pc_choice == ur_choice:
    print("It's a tie")
else:
    print("Is that even a thing?")
