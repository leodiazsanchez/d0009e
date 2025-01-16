from bounce import bounce
from tvärsumman import tvarsumman
from ekvationslösare import solve

def printMenu():  # Skriver ut menyn
    print()
    print("Menu")
    print()
    print("1: Bounce")
    print("2: Tvärsumman")
    print("3: Ekvationslösare")
    print("4: Exit program")

def f(x):
  return x**2-1

def menu(): 
    printMenu()  # Kallar på menyn
    # Låter användaren välja 1 av 4 val där 4 avslutar programmet
    option = int(input("Choose alternative:"))
    while option != 4:
        if option == 1:
            n = int(input("Nummer för bounce:"))
            bounce(n)
        elif option == 2:
            n = int(input("Tvärsumma av:"))
            print(tvarsumman(n))
        elif option == 3:
            x0 = int(input("Startvärde för ekvationslösare:"))
            print(solve(f,x0,0.0001))
        else:
           print("Invalid operation.")

        printMenu()
        option = int(input("Choose alternative:"))

menu()