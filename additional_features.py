import sys

phrase = (sys.argv[0])
filename = (sys.argv[1])


def start():  # launching the program and data import
    print("\nWprowadzanie danych rozpoczęte. Czy chcesz zaimportować plik?")
    answear = input("Wprowadź tak lub nie:\n")
    if answear == "tak":
        f = open(filename, "r", encoding="utf-8")
        f.readlines()
        for line in filename:
            print(line, end="")
        f.close()
        print(f"\nZmiany zostały zapisane w pliku: {filename}.")
    else:
        print("Dane nie zostały zaimportowane.")
