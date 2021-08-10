from accountant_classes import Warehouse

warehouse = Warehouse()
warehouse.launching()
warehouse.check_action()
warehouse.end()

print("Liczba wykonanych operacji:", (len(warehouse.actions)), "\nWprowadź zakres (od, do):")
start = int(input())
end = int(input())
print(warehouse.actions[start:end])
