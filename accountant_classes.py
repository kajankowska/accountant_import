import sys

filename = (sys.argv[0])
input_file = (sys.argv[1])
current_input = (sys.argv[2:])
print(sys.argv)


class Warehouse:
    def __init__(self):
        self.balance = 0
        self.storage = {}
        self.actions = []

    def launching(self):  # czytanie z pliku
        with open((sys.argv[0]), "r", encoding="utf-8") as file:
            for line in file:
                self.actions.append(line)
        print(f"\nWprowadzanie rozpoczęte. \nNastąpi import danych z pliku: {(sys.argv[0])}.\n")

    def balance(self, amount, comment):
        if self.balance + amount < 0:
            print("Brak środków na koncie.")
            return False
        self.balance += amount
        log = f'{"saldo"},{amount},{comment}'
        self.actions.append(log)
        return True

    def purchase(self, product, price, quantity):
        if self.balance < price * quantity:
            print("Niewystarczająca ilość środków na zakup")
            return False
        if product in self.storage:
            self.storage[product] += quantity
        else:
            self.storage[product] = quantity
        self.balance -= price * quantity
        if price < 0 or quantity < 0:
            print("Błąd! Ujemna wartość")
        log = f'{"zakup"},{product},{price},{quantity}'
        self.actions.append(log)
        return True

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
        self.balance += price * quantity
        log = f'{"sprzedaż"},{product},{price},{quantity}'
        self.actions.append(log)
        return True

    def stop(self):
        self.actions.append("stop")

    def end(self):  # zapisywanie do pliku
        with open((sys.argv[1]), "w", encoding="utf-8") as endfile:
            for line in self.actions:
                for i in line:
                    endfile.write(i)
        print(f"\nPlik {(sys.argv[1])} został zapisany.")
