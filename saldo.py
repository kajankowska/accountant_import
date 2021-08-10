from accountant_classes import Warehouse

warehouse = Warehouse()
warehouse.launching()
warehouse.check_action()
warehouse.end()

print("\nLista operacji:")
print("\n".join(warehouse.actions))
