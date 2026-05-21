from datetime import datetime

class ItemToPurchase:
    # Attributes set to default values
    def __init__(self, name = 'none', description = 'none', price = 0.00, quantity = 0):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity
    # Method to calculate and print the total cost of the item
    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"\033[1;35m {self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total:.2f} \033[0m".center(50))
        return total
    
class ShoppingCart:
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = list()
        
    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
        
    def remove_item(self, item_name):
        if item_name not in self.cart_items:
            print("\033[31m Item not found in cart. Nothing removed. \033[0m")
        else:
            self.cart_items.remove(item_name)
    def modify_item(self, ItemToPurchase):
        if ItemToPurchase.item_name not in self.cart_items:
            print("\033[31m Item not found in cart. Nothing modified. \033[0m")
        else:
            for item in self.cart_items:
                if ItemToPurchase.item_description != 'none':
                    item.item_description = ItemToPurchase.item_description
                if ItemToPurchase.item_price != 0.00:
                    item.item_price = ItemToPurchase.item_price
                if ItemToPurchase.item_quantity != 0:
                    item.item_quantity = ItemToPurchase.item_quantity
                break
    
    def get_num_items_in_cart(self):
        num_items = 0
        for items in self.cart_items:
            num_items += items.item_quantity
        return num_items
    
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost
    
# initialize an empty list to hold the items in the shopping cart, a boolean variable to control the while loop, and a counter to keep track of the number of items added to the cart
items = []
add_item = True
items_added = 0


# while loop to allow user to add items to the shopping cart until they choose to stop adding items
while add_item:
    # Prompt the user to add an item to the shopping cart
    input_item = input("Do you want to add an item to the shopping cart? (yes/no) ")
    
    # If the user inputs 'yes', prompt them to enter the item name, price, and quantity.
    # Ensure that the user inputs valid data for price and quantity. 
    if input_item.lower() == 'yes':
        print(f"Item {items_added + 1}")
        name = input("Enter the item name: ")
        try:
            price = float(input("Enter the item price: "))
            quantity = int(input("Enter the item quantity: "))
            description = input("Enter the item description: ")
        except ValueError:
            print("\033[31m Invalid input. Price and quantity must be a number. \033[0m")
            continue

        if price < 0 or quantity < 0:
            print("\033[31m Price or quantity cannot be negative. Please try again. \033[0m")
            continue
        # Create an instance of ItemToPurchase with the provided information and add it to the shopping cart. 
        item_to_purchase = ItemToPurchase(name, description, price, quantity)
        # Add the item to the shopping cart and display a message confirming that the item has been added.
        items.append(item_to_purchase)
        print(f"\033[32m {item_to_purchase.item_name} added to the cart. \033[0m")
        items_added += 1
    elif input_item.lower() == 'no':
        # If the user inputs 'no', exit the loop. 
        add_item = False
    else:
        # If the user inputs anything other than 'yes' or 'no', display an error message and prompt them again.
        print("\033[31m Invalid input. Please enter 'yes' or 'no'. \033[0m")

# After the user has finished adding items to the shopping cart, print out the total cost of all items in the cart by calling the print_item_cost() method for each item and summing the total cost.
print("\033[1;35m TOTAL COST: \033[0m".center(50))

total_cost = 0
for item in items:
    total_cost += item.print_item_cost()

print(f"\033[1;35m Total: ${total_cost:.2f} \033[0m".center(50))






customer_name = input("Enter customer's name: ")
current_date = datetime.now().strftime("%B %d, %Y")
shopping_cart = ShoppingCart(customer_name, current_date)            
            
print("\033[1;35m Shopping Cart Summary \033[0m".center(50))
print(f"\033[1;35m Customer Name: {customer_name} \033[0m".center(50))
print(f"\033[1;35m Today's Date: {current_date} \033[0m".center(50))
print("\033[1;35m Number of Items: {num_items} \033[0m".center(50))
print(f"\033[1;35m Total Cost: ${total_cost:.2f} \033[0m".center(50))



    

