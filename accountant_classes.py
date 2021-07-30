class Warehouse:
    def __init__(self):
        self.balance = 0
        self.products = {}
        self.actions = []


def balance(self, amount, comment):
    if self.balance + amount < 0:
        print("Brak środków na koncie.")
        return False
    log = f'{"saldo"} -- {amount} -- {comment}'
    self.actions.append(log)
    return True


def purchase(self, product, price, quantity):
    if self.balnce < price * quantity:
        print("Niewystarczająca ilość środków na zakup")
        return False
    if self.product in self.products:
        self.products[product] += quantity
    else:
        self.products[product] = quantity
    self.balance -= price * quantity
    if price < 0 or quantity < 0:
        print("Błąd! Ujemna wartość")
    log = f'{"zakup"} -- {product} -- {price} -- {quantity}'
    self.actions.append(log)
    return True


def sales(self, product, price, quantity):
    if product not in self.products:
        print("Towar niedostępny w magazynie.")
        return False
    if self.products[product] < quantity:
        print("Niewystarczająca ilość towaru w magazynie.")
        return False
    else:
        self.products[product] -= quantity
    if price < 0 or quantity < 0:
        print("Błąd! Ujemna wartość")
    log = f'{"sprzedaż"} -- {product} -- {price} -- {quantity}'
    self.actions.append(log)
    return True


def storage(self, product):
    for item in product:
        if item not in self.products:
            self.products[item] = 0
    for k, v in self.products.items():
        print(f"{k}: {v}.")


def review(self):
    print("Liczba wykonanych operacji:", (len(self.actions)), "\nWprowadź zakres (od, do):")
    start = int(input())
    end = int(input())
    print(self.actions[start:end])
    
