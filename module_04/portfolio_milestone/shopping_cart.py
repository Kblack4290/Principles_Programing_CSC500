#Step 1: Build the ItemToPurchase class with the following specifications:

# Attributes
# item_name (string)
# item_price (float)
# item_quantity (int)
# Default constructor
# Initializes item's name = "none", item's price = 0, item's quantity = 0
# Method
# print_item_cost()
# Example of print_item_cost() output:
# Bottled Water 10 @ $1 = $10


class ItemToPurchase:
    def __init__(self, name = 'none', price = 0.00, quantity = 0):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total:.2f}")
        return total

items = []
add_item = True
items_added = 0

while add_item:
    input_item = input("Do you want to add an item to the shopping cart? (yes/no)\n")
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
        
        item_to_purchase = ItemToPurchase(name, price, quantity)
        items.append(item_to_purchase)
        print(f"{item_to_purchase.item_name} added to the cart.")
        items_added += 1
    elif input_item.lower() == 'no':
        add_item = False
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

print("TOTAL COST")

total_cost = 0
for item in items:
    total_cost += item.print_item_cost()

print(f"Total: ${total_cost:.2f}")




