import sys

filename = (sys.argv[0])
input_file = (sys.argv[1])
current_input = (sys.argv[2:])
print(sys.argv)


class Warehouse:
    def __init__(self):
        self.balances = 0
        self.storage = {}
        self.actions = []
        self.inputs = []

    def launching(self):  # czytanie z pliku
        with open((sys.argv[1]), "r", encoding="utf-8") as file:
            for line in file:
                self.inputs.append(line.strip())
        print(f"\nWprowadzanie rozpoczęte. \nNastąpi import danych z pliku: {(sys.argv[1])}.")

    def check_action(self):
        while True:
            action = self.inputs.pop(0)
            if action == "saldo":
                amount = int(self.inputs.pop(0))
                comment = self.inputs.pop(0)
                self.balance(amount, comment)
            if action == "zakup":
                product = self.inputs.pop(0)
                price = int(self.inputs.pop(0))
                quantity = int(self.inputs.pop(0))
                self.purchase(product, price, quantity)
            if action == "sprzedaż":
                product = self.inputs.pop(0)
                price = int(self.inputs.pop(0))
                quantity = int(self.inputs.pop(0))
                self.sales(product, price, quantity)
            if action == "stop":
                self.actions.append("stop")
                break
            else:
                print("Niepoprawna operacja! Wprowadź ponownie")
                continue

    def balance(self, amount, comment):
        if self.balances + amount < 0:
            print("Brak środków na koncie.")
            return False
        self.balances += amount
        log = f'{"saldo"},{amount},{comment}'
        self.actions.append(log)

    def purchase(self, product, price, quantity):
        if self.balances < int(price * quantity):
            print("Niewystarczająca ilość środków na zakup")
            return False
        if product in self.storage:
            self.storage[product] += quantity
        else:
            self.storage[product] = quantity
        self.balances -= price * quantity
        if price < 0 or quantity < 0:
            print("Błąd! Ujemna wartość")
        log = f'{"zakup"},{product},{price},{quantity}'
        self.actions.append(log)

    def sales(self, product, price, quantity):
        if product not in self.storage:
            print("Towar niedostępny w magazynie.")
            return False
        if self.storage[product] < quantity:
            print("Niewystarczająca ilość towaru w magazynie.")
            return False
        else:
            self.storage[product] -= quantity
        if price < 0 or quantity < 0:
            print("Błąd! Ujemna wartość")
        self.balances += price * quantity
        log = f'{"sprzedaż"},{product},{price},{quantity}'
        self.actions.append(log)

    def end(self):  # zapisywanie do pliku
        with open((sys.argv[2]), "w", encoding="utf-8") as endfile:
            for line in self.actions:
                endfile.write(line)
        print(f"\nPlik {(sys.argv[2])} został zapisany.\n")
