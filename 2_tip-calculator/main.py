# Print welcome message.
print("Welcome to the tip calculator!")
# Request bill data.
total_bill = float(input("What was the total bill? $"))
percent_tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill? "))
# Calculate tip and total bill
tip = (percent_tip + 100) / 100
new_bill = total_bill * tip
# Split bill per person
unit_bill = new_bill / people
# Round the result to 2 decimal places.
new_unit_bill = round(unit_bill, 2)
# Print result
print(f"Each person should pay: ${new_unit_bill}")
