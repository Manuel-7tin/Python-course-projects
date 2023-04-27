# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Display welcome message
print("Welcome to the PyPassword Generator!")

# Request for inputs
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = []

# Create password
for letter in range(1, nr_letters+1):
    letters_n = random.randint(0, len(letters)-1)
    rand_letters = letters[letters_n]
    password.append(rand_letters)
for symbol in range(1, nr_symbols + 1):
    rand_symbols = random.choice(symbols)
    password += rand_symbols
for number in range(1, nr_numbers + 1):
    rand_numbers = random.choice(numbers)
    password += rand_numbers

# Secure password
random.shuffle(password)
new_password = ""
for char in password:
    new_password += char

# Display password
print(f"Your password is: {new_password}")
