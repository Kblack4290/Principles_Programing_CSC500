from datetime import datetime
import sys


class ItemToPurchase:
    # Attributes set to default values
    def __init__(
        self,
        item_name="none",
        item_price=0.00,
        item_quantity=0,
        item_description="none",
    ):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    # Method to calculate and print the total cost of the item
    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"\033[1;35m {self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total:.2f} \033[0m".center(50))
        return total


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = list()

    def add_items(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)
        print(f"\033[32m {item_to_purchase.item_name} added to the cart. \033[0m")
        for item in self.cart_items:
            print(item.item_name)

    def remove_item(self, item_name):
        if item_name not in self.cart_items:
            print("\033[31m Item not found in cart. Nothing removed. \033[0m")
        else:
            self.cart_items.remove(item_name)

    def modify_item(self, item_to_purchase):
        if item_to_purchase.item_name not in self.cart_items:
            print("\033[31m Item not found in cart. Nothing modified. \033[0m")
        else:
            for item in self.cart_items:
                if item_to_purchase.item_description != "none":
                    item.item_description = item_to_purchase.item_description
                if item_to_purchase.item_price != 0.00:
                    item.item_price = item_to_purchase.item_price
                if item_to_purchase.item_quantity != 0:
                    item.item_quantity = item_to_purchase.item_quantity
                break

    def get_num_items_in_cart(self):
        num_items = 0
        for items in self.cart_items:
            num_items += items.item_quantity
        return num_items

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_quantity * item.item_price
            item.print_item_cost()
        return total_cost

    def print_total(self):
        print(f"\033[1;35m OUTPUT SHOPPING CART\033[0m".center(50))
        print(f"\033[1;35m {customer_name}'s Shopping Cart - {current_date} \033[0m".center(50))
        print(f"\033[1;35m Number of Items: {shopping_cart.get_num_items_in_cart()} \033[0m".center(50))
        print(f"\033[1;35m Total: ${shopping_cart.get_cost_of_cart():.2f} \033[0m".center(50))

    def print_description(self):
        print(f"\033[1;35m OUTPUT ITEMS' DESCRIPTIONS\033[0m".center(50))
        print(f"\033[1;35m {customer_name}'s Shopping Cart - {current_date} \033[0m".center(50))
        print(f"\033[1;35m Item Descriptions \033[0m".center(50))

        for item in self.cart_items:
            print(f"\033[1;35m {item.item_name}: {item.item_description} \033[0m".center(50))


# initialize an empty list to hold the items in the shopping cart, a boolean variable to control the while loop, and a counter to keep track of the number of items added to the cart
add_item = True
items_added = 0
current_date = datetime.now().strftime("%B %d, %Y")
customer_name = input("Enter your name: ")
shopping_cart = ShoppingCart(customer_name, current_date)

def main():
    print(f"\033[1;35m Welcome to the shop!!\033[0m".center(50))
    print_menu(shopping_cart)

def print_menu(shopping_cart):
    menu = {
        "a": "Add item to cart",
        "r": "Remove item from cart",
        "c": "Change item quantity",
        "i": "Output items' descriptions",
        "o": "Output shopping cart",
        "q": "Quit",
    }
    print(f"\033[1;35m MENU \033[0m".center(50))
    for select in menu:
        print(f"\033[1;35m {select} - {menu[select]} \033[0m".center(50))
        
    menu_selection = input(f" Choose an Option: ")
    if(menu_selection == 'q'):
        print(f"\033[1;35m Goodbye!!! \033[0m".center(50))
        sys.exit()
        
if __name__ == "__main__":
    main()

# while loop to allow user to add items to the shopping cart until they choose to stop adding items
while add_item:
    # Prompt the user to add an item to the shopping cart
    input_item = input("Do you want to add an item to the shopping cart? (yes/no) ")

    # If the user inputs 'yes', prompt them to enter the item name, price, and quantity.
    # Ensure that the user inputs valid data for price and quantity.
    if input_item.lower() == "yes":
        print(f"Item {items_added + 1}")
        name = input("Enter the item name: ")
        try:
            price = float(input("Enter the item price: "))
            quantity = int(input("Enter the item quantity: "))
        except ValueError:
            print(
                "\033[31m Invalid input. Price and quantity must be a number. \033[0m"
            )
            continue
        if price < 0 or quantity < 0:
            print(
                "\033[31m Price or quantity cannot be negative. Please try again. \033[0m"
            )
            continue
        description = input("Add a description of the item: ")
        # Create an instance of ItemToPurchase with the provided information and add it to the shopping cart.
        item_to_purchase = ItemToPurchase(name, price, quantity, description)
        # Add the item to the shopping cart and display a message confirming that the item has been added.
        shopping_cart.add_items(item_to_purchase)
        items_added += 1
    elif input_item.lower() == "no":
        # If the user inputs 'no', exit the loop.
        add_item = False
    else:
        # If the user inputs anything other than 'yes' or 'no', display an error message and prompt them again.
        print("\033[31m Invalid input. Please enter 'yes' or 'no'. \033[0m")

# After the user has finished adding items to the shopping cart, print out the total cost of all items in the cart by calling the print_item_cost() method for each item and summing the total cost.

shopping_cart.print_total()
print()
shopping_cart.print_description()
print()

