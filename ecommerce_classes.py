from datetime import datetime
from random import randint
from customer import Customer

class Product:
    """
    Product Class
    """

    def __init__(self, name: str, product_id: str, price: float):
        self.name = name
        self.product_id = product_id
        self.price = float(price)
        # self.data = {self.product_id:{"Name": self.name, "Price": self.price, "Quantity": self.quantity}}

    def __post_init__(self) -> None:
        if self.price < 0:
            raise ValueError("price attribute must be greater than zero.")

    def __str__(self) -> str:
        return f"Name: {self.name}\nProduct_id: {self.product_id}\nPrice: {self.price}"

    def data_dict(self) -> dict:
        return {
            "Name": self.name,
            "Product_id": self.product_id,
            "Price": self.price,
        }

    def set_price(self, value) -> None:
        self.price = value


class Inventory:
    """ 
    Inventory structure: {product_1: quantity_1,
                         product_2: quantity_2,
                         product_3: quantity_3}
    """

    def __init__(self) -> None:
        self.inventory = {}

    def add_product(self, product: Product, quantity: int) -> dict:
        if product in self.inventory:
            self.inventory[product] += quantity
        else:
            self.inventory[product] = quantity

    def remove_product(self, product: Product, quantity: int):
        if product in self.inventory:
            if self.inventory[product] >= quantity:
                self.inventory[product] -= quantity
            else:
                raise ValueError("Not enough stock for product.")
        else:
            raise ValueError("Product not in inventory.")

    def value(self) -> float:
        total = 0
        for product, quantity in self.inventory.items():
            total += product.price*quantity
        return total


class Cart:
    """

    """

    def __init__(self) -> None:
        self.items = {}

    def add_product(self, product: Product, quantity: int = 1) -> dict:
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove_product(self, product: Product, quantity: int = 1) -> dict:
        if product in self.items:
            if self.items[product] >= quantity:
                self.items[product] -= quantity
            else:
                del self.items[product]

    def value(self) -> float:
        total = 0
        for product, quantity in self.items.items():
            total += product.price*quantity
        return total

    def get_items(self) -> dict:
        return self.items


class Order:
    """
    
    """
    def __init__(self, customer: Customer, cart: Cart) -> None:
        self.customer = customer
        self.status = "open"
        self.cart = cart
        self.creation_date = datetime.today()
        self.total_price = cart.value()

    def add_product(self, product: Product, quantity: int) -> None:
        self.cart.append((product, quantity))

    def checkout(self, inventory: Inventory) -> None:
        payment_success = self.process_payment()

        if payment_success:
            self.fulfill_order(inventory)
        else:
            raise ValueError("Payment was not successful")

    def process_payment(self):
        # Assume payment process is always successful
        return True

    def fulfill_order(self, inventory: Inventory):
        for product, quantity in self.cart.items.items():
            inventory.remove_product(product, quantity)
            print(f"Completed order for {quantity} {product.name}")
        self.status = "closed"


