import os
from models.inventory import Product


def load_products(path, inventory):
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line:
                    name, quantity = line.split("|")
                    product = Product(name, int(quantity))
                    inventory.add_product(product)

    except FileNotFoundError:
        pass


def save_products(path, inventory):
    # ✅ ensure folder exists before saving
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        for product in inventory.products:
            file.write(f"{product.name}|{product.quantity}\n")