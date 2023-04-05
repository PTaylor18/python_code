from ecommerce_classes import *
import json


def main() -> None:

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

    ps5 = list(inventory.inventory.keys())[0]
    xbx = list(inventory.inventory.keys())[1]

    paul = Customer("Paul", "Taylor", "pm.taylor18@gmail.com", "07480296417")

    cart = Cart()
    cart.add_product(ps5)
    cart.add_product(xbx)

    order = Order(paul, cart)
    order.checkout(inventory)


if __name__ == "__main__":
    main()
