from ecommerce_classes import *
import json
from random import choice, choices, randint


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
            1000
        )

    ps5 = list(inventory.inventory.keys())[0]
    xbx = list(inventory.inventory.keys())[1]
    ns = list(inventory.inventory.keys())[2]

    first_names = ["Walter", "Jesse", "Gus",
                   "Mike", "Saul", "Hank", "Skyler", "Hector"]
    last_names = ["White", "Pinkman", "Fring", "Ehrmantraut",
                  "Goodman", "Schrader", "White", "Salamanca"]

    for i in range(10):
        first_name = choice(first_names)
        last_name = choice(last_names)
        customer = Customer(first_name=first_name, last_name=last_name,
                            email=f"{first_name.lower()}{last_name.lower()}@email.com",
                            phone="07"+"".join(choices("0123456789", k=9))
                            )

        basket = Basket()
        basket.add_product(ps5, randint(1, 10))
        # basket.add_product(xbx, randint(1, 10))
        # basket.add_product(ns, randint(1, 10))

        order = Order(customer, basket)
        print(order.order_id)
        order.checkout(inventory)


if __name__ == "__main__":
    main()
