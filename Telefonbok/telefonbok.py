# Fixa alias
class PhoneBook:

    def __init__(self):  # Konstruktor med telefonbok i form av en katalog och en lista med kommandon och antal argument
        self.contacts = {}
        self.cmds = [("add", 2), ("lookup", 2), ("alias", 2), ("change", 2),("save", 1), ("load", 1), ("quit", 1), ("view", 1)]

    # -----HJÄLPMETODER----
    def strToList(self, string):
        return list(string)

    def lstToStr(self, lst):
        return ''.join(lst)

    def getValue(self, value):
        return self.contacts.get(value)

    def isInNames(self, key):  # Metod för att kolla om ett namn finns i telefonboken
        if key in self.contacts.keys():
            return True
        return False

    def isInNumbers(self, value):  # Metod för att kolla om ett numListmer finns i telefonboken
        if value in self.contacts.values():
            return True
        return False

    def update(self, name, number):  # Metod för att uppdatera telefonboken
        self.contacts.update({name:number})

    def getArgs(self, arg):  # Metod för att hitta hur många argument ett kommando ska ta
        for x in self.cmds:
            if arg == x[0]:
                return x[1]
        raise ValueError  # Kastar ett ValueError argumentet som skickas inte finns

    def isInCmd(self, cmd):  # Metod för att kolla om input är ett kommando
        for x in self.cmds:
            if cmd == x[0]:
                return True
        return False

    # -----UI-METODER----
    def add(self, name, number):  # Metod för att lägga till en person
        numList = self.strToList(number)
        if self.isInNames(name):
            print(name, "already exists")
        elif self.isInNumbers(numList):
            print(self.lstToStr(numList), "already exists")
        else:
            self.update(name, numList)

    def lookup(self, name):  # Metod för att hitta en person
        if not self.isInNames(name):
            print(name, "not found")
        else:
            number = self.getValue(name)
            print(self.lstToStr(number))

    def change(self, name, number):  # Metod för att byta namn på en person
        numList = self.strToList(number)
        if not self.isInNames(name):
            print(name, "not found")
        elif self.isInNumbers(numList):
            print(number, "already exists")
        else:
            value = self.getValue(name) # Hämtar listan från personen
            value[:] = numList # Ersätter värderna i listan med värdena i den nya listan.
            self.update(name, value)

    def alias(self, name, name2):  # Metod för att skapa alias
        if not self.isInNames(name) or self.isInNames(name) and self.isInNames(name2):
            print("name not found or duplicate name")
        else:
            value = self.getValue(name)
            self.update(name2, value)

    def save(self, filename):  # Metod för att spara telefonboken till en fil
        file = open(filename, "w")  # Öppna fil för skrivning
        for x in self.contacts.items(): # Får lista av tupler
            file.write(self.lstToStr(x[1]) + ";" + x[0] + ";" + "\n")  # Filformat
        file.close()  # Stänger filen

    def load(self, filename):  # Metod för att läsa in en telefonbok från fil
        file = open(filename, "r")  # Öppna fil för läsning
        self.contacts = {}  # Tömmer telefonboken
        for line in file:
            string = line.strip()  # Tar bort alla whitespace innan och efter
            elements = string.split(";") # Splitar strängen vid ";" och gör det till en lista av substrängarna
            number = self.strToList(elements[0]) # Vi får nummret som str men vi gör om den till list 
            name = elements[1] 
            self.contacts.update({name: number}) # Uppdatera telefonboken med kontakterna
        file.close()

    def main(self):  # UI metoden
        while True:  # While loop som körs tills vi skickar "break"
            string = input("phoneBook> ")  # Promt
            args = string.split()  # Delar upp strängen till lista av substängar vid whitespace

            if args == []:  # Om listan är tom visar vi en ny promt
                continue

            # Om det första argumentet inte är ett kommando
            elif not self.isInCmd(args[0]):
                print("Command not found.")

            elif args[0] == "view":  # DEBUG VERKYTYG!!!!
                print(self.contacts)

            elif args[0] == "quit":  # Quit kommando som avslutar programmet
                break

            try:  # Kommandon som körs i en try-catch block. IndexError och FileNotFoundError kan uppstå och de fångas
                if args[0] == "add":
                    self.add(args[1], args[2])

                elif args[0] == "lookup":
                    self.lookup(args[1])

                elif args[0] == "alias":
                    self.alias(args[1], args[2])

                elif args[0] == "change":
                    self.change(args[1], args[2])

                elif args[0] == "save":
                    self.save(args[1])

                elif args[0] == "load":  # Här kan det uppstå FileNotFoundError
                    self.load(args[1])

            except IndexError:  # Fångar IndexError
                try:
                    args_taken = self.getArgs(args[0])
                except ValueError:  # Fångar ValueError från getArgs()
                    print("Command to function 'getArgs' does not exist!")
                    continue
                args_given = len(args)-1
                print("Command", args[0], "takes", args_taken,
                      "argument(s).", args_given, "given.")
                continue

            except FileNotFoundError:  # Fångar FileNotFoundError
                print("File not found")
                continue


phoneBook = PhoneBook()  # Skapar en ny instans av klassen PhoneBook med namnet phoneBook
phoneBook.main()
