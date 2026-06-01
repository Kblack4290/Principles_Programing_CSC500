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

    # Method to remove an item from the shopping cart
    def remove_item(self, item_name):

        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                print(f"\033[32m {item_name} removed from the cart. \033[0m")
                return
        print("\033[31m Item not found in cart. Nothing removed. \033[0m")

    # Method to modify an item in the shopping cart
    def modify_item(self, item_to_purchase):
        item_found = False
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                item_found = True
                if item_to_purchase.item_price != 0:
                    item.set_item_price(item_to_purchase.item_price)
                if item_to_purchase.item_quantity != 0:
                    item.set_item_quantity(item_to_purchase.item_quantity)
                if item_to_purchase.item_description != "none":
                    item.set_item_description(item_to_purchase.item_description)
                if item_to_purchase.item_name != "none":
                    item.set_item_name(item_to_purchase.item_name)
                print(f"\033[32m {item.item_name} modified in the cart. \033[0m")
                return
        if not item_found:
            print("\033[31m Item not found in cart. Nothing modified. \033[0m")            

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
        print()
        print(f"\033[1;35m OUTPUT SHOPPING CART\033[0m".center(50))
        print(f"\033[1;35m {self.customer_name}'s Shopping Cart - {self.current_date} \033[0m".center(50))
        
        if not self.cart_items:
            print(f"\033[1;35m SHOPPING CART IS EMPTY \033[0m".center(50))
            return
        
        print(f"\033[1;35m Number of Items: {self.get_num_items_in_cart()} \033[0m".center(50))
        print(f"\033[1;35m Total: ${self.get_cost_of_cart():.2f} \033[0m".center(50))

    # Method to print the descriptions of the items in the shopping cart
    def print_description(self):
        print()
        print(f"\033[1;35m OUTPUT ITEMS' DESCRIPTIONS\033[0m".center(50))
        print(f"\033[1;35m {self.customer_name}'s Shopping Cart - {self.current_date} \033[0m".center(50))
        print(f"\033[1;35m Item Descriptions \033[0m".center(50))

        for item in self.cart_items:
            print(f"\033[1;35m {item.item_name}: {item.item_description} \033[0m".center(50))


