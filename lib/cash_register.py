class CashRegister:
    def __init__(self, discount=0):
        """Initialize a CashRegister instance with an optional discount."""
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, item_name, price, quantity=1):
        """Adds items to the register, updates total and stores transaction details."""
        self.total += price * quantity
        self.items.extend([item_name] * quantity)
        self.last_transaction_amount = price * quantity

    def apply_discount(self):
        """Applies a discount if available and prints the updated total."""
        if self.discount:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")  # Fix format
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """Removes the last added transaction from the total."""
        self.total -= self.last_transaction_amount
        self.last_transaction_amount = 0  # Reset the last transaction

    def get_total(self):
        """Returns the total amount in the register."""
        return self.total
