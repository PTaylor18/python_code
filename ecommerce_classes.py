import json
from datetime import datetime
from random import randint


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

    def increase_quantity(self, number: int) -> None:
        if type(number) != int:
            raise TypeError("quantity must be an integer")
        self.quantity += number

    def decrease_quantity(self, number: int) -> None:
        if type(number) != int:
            raise TypeError("quantity must be an integer")
        if number > self.quantity:
            raise ValueError("quantity cannot go below zero.")
        self.quantity -= number

    def set_quantity(self, number: int) -> None:
        if type(number) != int:
            raise TypeError("quantity must be an integer")
        self.quantity = number


class Inventory:
    """ 
    Inventory structure: {product_id_1:[product_object_1, quantity_1],
                         product_id_2:[product_object_2, quantity_2]}
    """

    def __init__(self) -> None:
        self.inventory = {}

    def add_product(self, product: Product, quantity: int) -> list:
        self.inventory.update({product.product_id: [product, quantity]})

    def remove_product(self):
        pass

    def value(self) -> float:
        return sum(
            product[0].price*product[1] for product in self.inventory.values()
        )

    def product_value(self, product_id_key: str) -> float:
        return self.inventory[product_id_key][0].price * self.inventory[product_id_key][1]


class Orders:
    def __init__(self) -> None:
        self.status = "open"
        self.products = []
        self.creation_date = datetime.today()

    def add_product(self, product: Product, quantity: int) -> None:
        self.products.append((product, quantity))

    def total_price(self) -> float:
        return sum(i[0].price*i[1] for i in self.products)

    def confirm_order(self, inventory: Inventory) -> None:
        pass


def inventory_check(order: Orders, inventory: Inventory) -> bool:
    """
        Takes in an order class and inventory class and checks if enough stock in inventory to complete order.
    """
    fail_check = False
    for i in order.products:
        if i[0].product_id in inventory.inventory.keys():
            if i[1] > inventory.inventory[i[0].product_id][1]:
                print(f"Not enough stock for product: {i[0].name}")
                fail_check = True
            else:
                print(f"Enough stock for product: {i[0].name}")
        else:
            print("Product not in inventory.")
            fail_check = True

    if fail_check:
        return False
    else:
        return True


with open("products_with_id.json", mode="r") as f:
    product_data = json.load(f)

inventory = Inventory()
for product in product_data["product"]:
    inventory.add_product(
        Product(
            product["name"],
            product["product_id"],
            product["price"],
        ),
        randint(1, 10)
    )

print(inventory.inventory)
# print(inventory.inventory['2bbcfa74-a261-4748-87a3-c923b696eb0c'][0].__str__())
# print(inventory.product_value(
#     '2bbcfa74-a261-4748-87a3-c923b696eb0c'))
# print(inventory.value())

ps5 = Product("PS5", "2bbcfa74-a261-4748-87a3-c923b696eb0c", "479")
xbx = Product("Xbox Series X", "5b80d4d5-71ac-4512-a01b-55db4d9700a4", "420")

order1 = Orders()

for k in [ps5, xbx]:
    order1.add_product(k, 5)
# print(order1.products)
x = inventory_check(order1, inventory)
print(x)
#  print(inventory.inventory[0].data_dict())
# print(inventory.value())
# print([product.product_id for product in inventory.inventory])
# print([products.product_id for a, products in enumerate(inventory.inventory)])

# inventory.inventory[0].decrease_quantity(6)
# print(inventory.inventory[0].quantity)

# inventory.inventory[0].set_price(500)
# print(inventory.inventory[0].price)

# print(inventory.value())
