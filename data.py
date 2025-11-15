class Product:
    def __init__(self, type:str, quantity: int, price: float):
        self.type = type
        self.quantity = quantity
        self.price = price
        self.validate_arguments()

    def validate_arguments(self):
        if self.price < 0 or self.quantity < 0:
            raise ValueError("Price or Quantity incorrect")

    def __repr__(self):
        return f"{'Type:':<10} {self.type:^10} {'Quantity:':<10} {self.quantity:^10} {'Price':<10} {self.price:^10}\n"

class Inventory:
    def __init__(self):
        self.inventary =[
            Product(type="Chicken", quantity=1, price= 50)
        ]

    def add_product_to_inventory(self, Type:str, quantity:int, price:float):
        new_product = Product(Type, quantity, price)
        self.inventary.append(new_product)

    def delete_product(self, type:str, quantity_to_delete:int = 1, delete_all:bool = False):
        for product in self.inventary:
            if product.type == type:
                if delete_all:
                    self.inventary.remove(product)
                else:
                    if product.quantity < quantity_to_delete:
                        raise Exception("Invalid operation")
                    product.quantity -= quantity_to_delete


    def get_product(self, type:str):
        for product in self.inventary:
            if product.type == type:
                return product

        

    def show_inventary(self):
        print(self.inventary)








