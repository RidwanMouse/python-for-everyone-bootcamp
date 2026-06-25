# Fatima Mohamed Omar
#waa system yar dukaan ah 

from dataclasses import dataclass


@dataclass
class Product:
    name: str
    quantity: int

    def __str__(self):
        return f"{self.name} - Quantity: {self.quantity}"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        if not self.products:
            print("No products available.")
        else:
            for product in self.products:
                print(product)

    def update_product(self, name, quantity):
        for product in self.products:
            if product.name.lower() == name.lower():
                product.quantity = quantity
                return True

        return False

    def remove_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                self.products.remove(product)
                return True

        return False