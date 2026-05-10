class ItemToPurchase:
    # Attributes set to default values
    def __init__(self, name = 'none', price = 0.00, quantity = 0):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
    # Method to calculate and print the total cost of the item
    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total:.2f}")
        return total
    
# initialize an empty list to hold the items in the shopping cart, a boolean variable to control the while loop, and a counter to keep track of the number of items added to the cart
items = []
add_item = True
items_added = 0

# while loop to allow user to add items to the shopping cart until they choose to stop adding items
while add_item:
    # Prompt the user to add an item to the shopping cart
    input_item = input("Do you want to add an item to the shopping cart? (yes/no)\n")
    
    # If the user inputs 'yes', prompt them to enter the item name, price, and quantity.
    # Ensure that the user inputs valid data for price and quantity. 
    if input_item.lower() == 'yes':
        name = input("Enter the item name:\n")
        try:
            price = float(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))
        except ValueError:
            print("Invalid input. Price and quantity must be a number.")
            continue

        if price < 0 or quantity < 0:
            print("Price or quantity cannot be negative. Please try again.")
            continue
        # Create an instance of ItemToPurchase with the provided information and add it to the shopping cart. 
        item_to_purchase = ItemToPurchase(name, price, quantity)
        # Add the item to the shopping cart and display a message confirming that the item has been added.
        items.append(item_to_purchase)
        print(f"{item_to_purchase.item_name} added to the cart.")
        items_added += 1
    elif input_item.lower() == 'no':
        # If the user inputs 'no', exit the loop. 
        add_item = False
    else:
        # If the user inputs anything other than 'yes' or 'no', display an error message and prompt them again.
        print("Invalid input. Please enter 'yes' or 'no'.")

# After the user has finished adding items to the shopping cart, print out the total cost of all items in the cart by calling the print_item_cost() method for each item and summing the total cost.
print("TOTAL COST")

total_cost = 0
for item in items:
    total_cost += item.print_item_cost()

print(f"Total: ${total_cost:.2f}")




