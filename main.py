from data import Product, Inventory

def main():
    inventory_1 = Inventory()

    print("------------------INVENTORY-----------------")
    inventory_1.show_inventory()

    inventory_1.add_product(type="Pig", quantity=2, price=120)
    inventory_1.add_product(type="Cow", quantity=1, price=200)
    inventory_1.add_product(type="Goat", quantity=5, price=170)

    print("------------------INVENTORY-----------------")
    inventory_1.show_inventory()

    print("------------------GET PRODUCT-----------------")
    print(inventory_1.get_product(type="Cow"))

    inventory_1.delete_product(type="Pig", delete_all=True)

    print("------------------INVENTORY-----------------")
    inventory_1.show_inventory()


if __name__ == "__main__":
    main()
