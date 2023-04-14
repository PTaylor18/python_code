"""
    Generates a unique product id
"""
import json
from uuid import uuid4


def id_generator(
    data: dict[str, list[dict[str, str]]]
) -> dict[str, list[dict[str, str]]]:
    """
    Function to generate a product id for each product in the json data.
    """
    for product in data["product"]:
        if product["product_id"] is None:  # type: ignore
            product["product_id"] = str(uuid4())  # type: ignore
        else:
            continue
    return data


with open("products.json", mode="r") as f:
    product_data = json.load(f)

new_data = id_generator(product_data)

with open("products_with_id.json", mode="w") as f:
    json.dump(new_data, f, indent=4)
