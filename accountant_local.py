account_history = []


class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class Warehouse:
    def __init__(self, stock, current_account):
        self.stock = stock
        self.account = current_account
        self.products = {}


def product_purchase(self, new_product, price):
    if self.account.chceck_balance < price * new_product.quantity:
        print("Niewystarczająca ilość środków na zakup")
    if new_product.name in self.products:
        self.products[new_product.name] += new_product.quantity
    else:
        self.products[new_product.name] = new_product
        account_history.append(f"Zakup: {new_product.name}, {price}, {new_product.quantity}")


class Account:
    def __init__(self):
        self.balance = 0

def check_balance(self, amount):
    if self.balance + amount < 0:
        return False
    self.balance += amount
    return True
