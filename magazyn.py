from accountant_classes import Warehouse

warehouse = Warehouse()
warehouse.launching()
warehouse.check_action()
warehouse.end()

print("\nStan produktów w magazynie:")
for k, v in warehouse.storage.items():
    print("{}: {}".format(k, v))
