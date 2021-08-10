from accountant_classes import Warehouse

warehouse = Warehouse()
warehouse.launching()
warehouse.check_action()
warehouse.end()

print(f"Stan konta po wykonanych operacjach: {warehouse.balances}")
