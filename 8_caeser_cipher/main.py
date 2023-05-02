alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    # Decide behaviour based on user input
    if cipher_direction == "decode":
        shift_amount *= -1
    # Create encrypted message
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
            # Display encrypted message
    print(f"Here's the {cipher_direction}d result: {end_text}")


# TODO-1: Import and print the logo from art.py when the program starts.
import art

print(art.logo)

# Try creating a while loop that continues to execute the program if the user types 'yes'.
cont = "yes"
while cont == "yes":
    # Request users name and honour user with a greeting.
    name = input("What is your name? ")
    print(f"Welcome {name}")
    # Request action.
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    # Request message and shift number
    shift = int(input("Type the shift number:\n"))

    # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    if shift > 26:
        shift %= 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    # TODO-4: Figure out a way to ask the user if they want to restart the cipher program?
    cont = input("Do you wish to continue? Type yes to continue, otherwise type no\n ").lower()
print(f"Goodbye {name}")
