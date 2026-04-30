# Critical Thinking: Part One

# Write a program that calculates the total amount of a meal purchased at a restaurant. 
# The program should ask the user to enter the charge for the food and then calculate the amounts with an 18 percent tip and 7 percent sales tax. 
# Display each of these amounts and the total price.

# User inputs a valid float
# If the user inputs an invalid value, the program will display an error message and exit.

try:
    meal_charge = float(input("Enter the charge for the food: "))
except ValueError:
    print("Invalid input. Please enter a numeric value for the meal charge.")
    exit()

# Assign calculated values to appropriate variables
# Calculate tip, tax, and total price
tip = meal_charge * 0.18 
tax = meal_charge * 0.07
total_price = meal_charge + tip + tax

# Display the calculated amounts with appropriate formatting
print("Charge for the food: $", f"{meal_charge:.2f}")
print("Tip (18%): $", f"{tip:.2f}")
print("Sales Tax (7%): $", f"{tax:.2f}")
print("Total Price: $", f"{total_price:.2f}")

