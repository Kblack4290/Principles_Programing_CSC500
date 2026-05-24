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
    
    # Attributes set to default values
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = list()

    # Method to add an item to the shopping cart
    def add_items(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)
        print(f"\033[32m {item_to_purchase.item_name} added to the cart. \033[0m")
        for item in self.cart_items:
            print(item.item_name)

    # Method to remove an item from the shopping cart
    def remove_item(self, item_name):

        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                print(f"\033[32m {item_name} removed from the cart. \033[0m")
            else:
                print("\033[31m Item not found in cart. Nothing removed. \033[0m")

    # Method to modify an item in the shopping cart
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

    # Method to calculate the total number of items in the shopping cart
    def get_num_items_in_cart(self):
        num_items = 0
        for items in self.cart_items:
            num_items += items.item_quantity
        return num_items

    # Method to calculate the total cost of the items in the shopping cart
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_quantity * item.item_price
            item.print_item_cost()
        return total_cost

    # Method to print the total cost of the items in the shopping cart
    def print_total(self):
        print(f"\033[1;35m OUTPUT SHOPPING CART\033[0m".center(50))
        print(f"\033[1;35m {customer_name}'s Shopping Cart - {current_date} \033[0m".center(50))
        print(f"\033[1;35m Number of Items: {shopping_cart.get_num_items_in_cart()} \033[0m".center(50))
        print(f"\033[1;35m Total: ${shopping_cart.get_cost_of_cart():.2f} \033[0m".center(50))

    # Method to print the descriptions of the items in the shopping cart
    def print_description(self):
        print(f"\033[1;35m OUTPUT ITEMS' DESCRIPTIONS\033[0m".center(50))
        print(f"\033[1;35m {customer_name}'s Shopping Cart - {current_date} \033[0m".center(50))
        print(f"\033[1;35m Item Descriptions \033[0m".center(50))

        for item in self.cart_items:
            print(f"\033[1;35m {item.item_name}: {item.item_description} \033[0m".center(50))

# Main function to run the shopping cart program
current_date = datetime.now().strftime("%B %d, %Y")
customer_name = input("Enter your name: ")
shopping_cart = ShoppingCart(customer_name, current_date)

# The main function to run the shopping cart program, which welcomes the user and displays the menu options.
def main():
    print(f"\033[1;35m Hi {customer_name}! Welcome to the shop!!\033[0m".center(50))
    print_menu(shopping_cart)

# Function to display the menu options and handle user input for the shopping cart program.
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
    
    # Use a series of if-elif statements to determine which menu option the user selected and call the appropriate method on the shopping cart object.
    if(menu_selection == 'q'):
        print(f"\033[1;35m Thank you for shopping with us! Have a great day! \033[0m".center(50))
        sys.exit()
        
    elif(menu_selection == 'a'):
        add_item = True
        items_added = 0
        # Use a while loop to allow the user to add multiple items to the shopping cart until they choose to stop.
        while add_item:

            if items_added == 0:
                input_item = input("Do you want to add an item to the shopping cart? (yes/no) ")
            else:
                input_item = input("Do you want to add another item to the shopping cart? (yes/no) ")

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

                # Create an instance of the ItemToPurchase class with the user's input and add it to the shopping cart.
                item_to_purchase = ItemToPurchase(name, price, quantity, description)
                shopping_cart.add_items(item_to_purchase)
                items_added += 1

            elif input_item.lower() == "no":
                # If the user inputs 'no', exit the loop and return to the main menu.
                add_item = False
            else:
                # If the user inputs anything other than 'yes' or 'no', display an error message and prompt them again.
                print("\033[31m Invalid input. Please enter 'yes' or 'no'. \033[0m")

    elif(menu_selection == 'r'):
        item_name = input("Enter the name of the item you want to remove: ")
        shopping_cart.remove_item(item_name)
    elif(menu_selection == 'c'):
        item_name = input("Enter the name of the item you want to modify: ")
        shopping_cart.modify_item(item_name)
    elif(menu_selection == 'i'):
        # Call the print_description method to display the descriptions of the items in the shopping cart.
        shopping_cart.print_description()
    elif(menu_selection == 'o'):
        # Call the print_total method to display the total cost of the items in the shopping cart.
        shopping_cart.print_total()
    else:
        print(f"\033[31m Invalid option. Please try again. \033[0m".center(50))
    
    print()
    print_menu(shopping_cart)
if __name__ == "__main__":
    main()

