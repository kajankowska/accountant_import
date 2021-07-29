import sys

filename = (sys.argv[1])
print(sys.argv[1])


def start():
    print("\nWprowadzanie danych rozpoczęte. Czy chcesz zaimportować plik?")
    answear = input("Wprowadź TAK lub NIE\n")
    if answear == "TAK":
        print("Nastąpi import danych")
        data_import()
    else:
        print("Dane nie zostały zaimportowane!")


def data_import():
    fd = open(filename)
    fd.readlines()

