from accountant_classes import Warehouse

warehouse = Warehouse()
warehouse.launching()
warehouse.check_action()
warehouse.end()

print("\n".join(warehouse.actions))
print(warehouse.purchase)
print(warehouse.inputs)
