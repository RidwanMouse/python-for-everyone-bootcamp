# Personal Catalog Program by Abdullahi4444
# This program lets users add, list, save, and load a small book catalog.

from dataclasses import dataclass
import os


@dataclass
class CatalogItem:
    title: str
    year: int

    def __str__(self):
        return f"{self.title} ({self.year})"


class Catalog:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def list_all(self):
        if not self.items:
            print("No books in the catalog yet.")
        else:
            for item in self.items:
                print(item)


def load_catalog(path, catalog):
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 2:
                    title = parts[0]
                    year = int(parts[1])
                    catalog.add_item(CatalogItem(title, year))
    except FileNotFoundError:
        pass


def save_catalog(path, catalog):
    with open(path, "w", encoding="utf-8") as file:
        for item in catalog.items:
            file.write(f"{item.title}|{item.year}\n")


def main():
    catalog_file = os.path.join(os.path.dirname(__file__), "catalog.txt")
    catalog = Catalog()
    load_catalog(catalog_file, catalog)

    while True:
        print("\nMy catalog - books")
        print("1) Add  2) List  3) Save  4) Quit")
        choice = input("Pick: ")

        if choice == "1":
            title = input("Title: ")
            year_text = input("Year: ")

            try:
                year = int(year_text)
                catalog.add_item(CatalogItem(title, year))
                print("Book added.")
            except ValueError:
                print("Please enter the year as a number.")
        elif choice == "2":
            catalog.list_all()
        elif choice == "3":
            save_catalog(catalog_file, catalog)
            print("Saved.")
        elif choice == "4":
            save_catalog(catalog_file, catalog)
            print("Saved. Bye!")
            break
        else:
            print("Invalid choice. Please pick 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
