from models.inventory import Product, Inventory
from utils.utility import load_products, save_products


def main():
    path = "data/stock.txt"

    inventory = Inventory()

    load_products(path, inventory)

    while True:
        print("\nInventory Stock Management System")
        print("1 = Add Product")
        print("2 = View Products")
        print("3 = Update Product Quantity")
        print("4 = Remove Product")
        print("5 = Save")
        print("6 = Quit")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Enter product name: ")

            try:
                quantity = int(input("Enter quantity: "))

                product = Product(name, quantity)
                inventory.add_product(product)

                print("Product added successfully.")

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            inventory.list_products()

        elif choice == "3":
            name = input("Enter product name to update: ")

            try:
                quantity = int(input("Enter new quantity: "))

                updated = inventory.update_product(name, quantity)

                if updated:
                    print("Product updated.")
                else:
                    print("Product not found.")

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            name = input("Enter product name to remove: ")

            removed = inventory.remove_product(name)

            if removed:
                print("Product removed.")
            else:
                print("Product not found.")

        elif choice == "5":
            save_products(path, inventory)
            print("Inventory saved.")

        elif choice == "6":
            save_products(path, inventory)
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")


main()