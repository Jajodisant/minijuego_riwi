class Product:
    def __init__(self, type: str, quantity: int, price: float):
        self.type = type
        self.quantity = quantity
        self.price = price
        self.validate_arguments()

    def validate_arguments(self):
        if self.price < 0:
            raise ValueError("El precio no puede ser negativo.")
        if self.quantity < 0:
            raise ValueError("La cantidad no puede ser negativa.")

    def __repr__(self):
        return (
            f"Type: {self.type:<10} | "
            f"Quantity: {self.quantity:<5} | "
            f"Price: {self.price:<5}\n"
        )


class Inventory:
    def __init__(self):
        # Inventario inicial (ejemplo, lo usarán para comenzar el juego)
        self.inventory = [
            Product(type="Chicken", quantity=1, price=50)
        ]

    # -------------------------------
    # Agregar productos al inventario
    # -------------------------------
    def add_product(self, type: str, quantity: int, price: float):
        product = self.get_product(type)

        # Si ya existe, aumentar cantidad
        if product:
            product.quantity += quantity
        else:
            new_product = Product(type, quantity, price)
            self.inventory.append(new_product)

    # -------------------------------
    # Eliminar productos
    # -------------------------------
    def delete_product(self, type: str, quantity_to_delete: int = 1, delete_all: bool = False):
        product = self.get_product(type)

        if not product:
            raise ValueError("El producto no existe en el inventario.")

        if delete_all:
            self.inventory.remove(product)
            return

        if quantity_to_delete <= 0:
            raise ValueError("Cantidad inválida.")

        if product.quantity < quantity_to_delete:
            raise ValueError("No hay suficiente cantidad para eliminar.")

        product.quantity -= quantity_to_delete

        # Si llega a 0, eliminarlo automáticamente
        if product.quantity == 0:
            self.inventory.remove(product)

    # -------------------------------
    # Buscar producto
    # -------------------------------
    def get_product(self, type: str):
        for product in self.inventory:
            if product.type.lower() == type.lower():
                return product
        return None

    # -------------------------------
    # Mostrar inventario
    # -------------------------------
    def show_inventory(self):
        if not self.inventory:
            print("Inventario vacío.")
            return

        print("\n----- INVENTARIO -----")
        for p in self.inventory:
            print(p)
