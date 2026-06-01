class ItemToPurchase:
    
    # Attributes set to default values
    def __init__(
        self,
        item_name="none",
        item_price=0.00,
        item_quantity=0,
        item_description="none",
    ):
        self.set_item_name(item_name)
        self.set_item_price(item_price)
        self.set_item_quantity(item_quantity)
        self.set_item_description(item_description)
        
    # Method to calculate and print the total cost of the item
    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"\033[1;35m {self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total:.2f} \033[0m".center(50))
        return total
    
    # Adding setter methods for dynamic modification of item attributes
    def set_item_name(self, item_name):
        self.item_name = item_name

    def set_item_price(self, item_price):
        self.item_price = item_price
    
    def set_item_quantity(self, item_quantity):
        self.item_quantity = item_quantity
    
    def set_item_description(self, item_description):
        self.item_description = item_description