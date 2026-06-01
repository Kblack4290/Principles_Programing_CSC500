import sys
from datetime import datetime
from item_to_purchase import ItemToPurchase
from shopping_cart import ShoppingCart

# Main function to run the shopping cart program
current_date = datetime.now().strftime("%B %d, %Y")
customer_name = input("Enter your name: ").title()
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
        "c": "Change item details",
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
                name = input("Enter the item name: ").title()
                try:
                    price = float(input("Enter the item price: "))
                    quantity = int(input("Enter the item quantity: "))
                except ValueError:
                    print("\033[31m Invalid input. Price and quantity must be a number. \033[0m")
                    continue
                if price < 0 or quantity < 0:
                    print("\033[31m Price or quantity cannot be negative. Please try again. \033[0m")
                    continue
                description = input("Add a description of the item: ").title()

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
        print(f"\033[1;35m REMOVE ITEM FROM CART\033[0m".center(50))
        item_name = input("Enter the name of the item you want to remove: ").title()
        shopping_cart.remove_item(item_name)
    elif(menu_selection == 'c'):
        print(f"\033[1;35m MODIFY ITEM IN CART\033[0m".center(50))
        item_name = input("Enter the name of the item you want to modify: ").title()

        # Get original values of the item to be modified
        original_item = None
        for item in shopping_cart.cart_items:
            if item.item_name == item_name:
                original_item = item
                break
        
        if original_item is None:
            print("\033[31m Item not found in cart. Nothing modified. \033[0m")
        else:
            price_input = input(f"Enter new price or press Enter to keep current the price at \033[1m${original_item.item_price:.2f}\033[0m: ")
            quantity_input = input(f"Enter new quantity or press Enter to keep the current quantity of \033[1m{original_item.item_quantity}\033[0m: ")
            description_input = input(f"Enter new description or press Enter to keep the current description \033[1m{original_item.item_description}\033[0m: ").title()

            try:
                item_price = float(price_input) if price_input.strip() else original_item.item_price
                item_quantity = int(quantity_input) if quantity_input.strip() else original_item.item_quantity
            except ValueError:
                print("\033[31m Invalid input. Price and quantity must be numbers. \033[0m")
                print_menu(shopping_cart)
                return

            item_description = description_input.strip() if description_input.strip() else original_item.item_description

            modify_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            shopping_cart.modify_item(modify_item)
        
    elif(menu_selection == 'i'):
        # Call the print_description method to display the descriptions of the items in the shopping cart.
        shopping_cart.print_description()
        input("Press Enter to return to the menu...")
    elif(menu_selection == 'o'):
        # Call the print_total method to display the total cost of the items in the shopping cart.
        shopping_cart.print_total()
        input("Press Enter to return to the menu...")
    else:
        print(f"\033[31m Invalid option. Please try again. \033[0m".center(50))
    
    print()
    print_menu(shopping_cart)
    
    
if __name__ == "__main__":
    main()

