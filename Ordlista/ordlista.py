#---------MENY---------#

def printMenu():  # Skriver ut menyn
    print()
    print("Menu for dictionary")
    print()
    print("1: Insert")
    print("2: Lookup")
    print("3: Delete")
    print("4: Exit program")


def menu(insert, lookup, delete): #Tar in de 3 funktionerna som argument från de 3 olika lösningarna
    printMenu() #Skriver ut menyn
    option = int(input("Choose alternative:")) #Låter användaren välja mellan de olika valen
    while option != 4:
        if option == 1:
            insert()
        elif option == 2:
            lookup()
        elif option == 3:
            delete()
        else:
            print("Invalid operation.")

        printMenu()
        option = int(input("Choose alternative:"))

#---------ORDLISA MED LISTOR---------#


def main_dic():  # Main funktionen för list versionen av programmet

    words = []  # Lista som innehåller alla ord
    descriptions = []  # Lista som innehåller alla förklaringar

    def insert_dic():  # Anropas om användaren väljer att lägga till ett ord (Val 1)
        word = input("Word to insert: ")
        if word in words:  # Kollar om ordet redan finns i listan
            print("Error: Word already exists!")
        else:
            # Lägger till ordet och förklaringen om ordet inte finns i listan
            words.append(word)
            desc = input("Description of word: ")  # Tar in förklaringen
            descriptions.append(desc)

    def lookup_dic():  # Anropas om användaren väljer att söka efter ett ord (Val 2)
        search = input("Word to lookup: ")
        if search not in words:  # Kollar om ordet inte finns i listan
            print("Error: Word does not exists!")
        else:
            # Hämtar ordets index för att visa den matchande förklaringen för användaren
            index = words.index(search)
            print("Description for",search,": ",descriptions[index])

    def delete_dic():  # Anropas om användaren väljer att bort ett ord (Val 3)
        word = input("Word to delete: ")
        if word not in words:  # Kollar om ordet inte finns i listan
            print("Error: Word does not exists!")
        else:
            # Hämtar ordets index för att ta bort ordet och förklaringen från listorna
            index = words.index(word)
            words.pop(index)
            descriptions.pop(index)
            print(word, "was sucessfully deleted.")

    menu(insert_dic, lookup_dic, delete_dic)

#---------ORDLISTA MED DICTIONARY---------#


def main_dic2():  # Huvudfunktionen för dictionary version av programmet

    dictionary = {}  # Dictionary med våra ord och förklaringar

    def insert_dic2():  # Anropas om användaren väljer att lägga till ett ord (Val 1)
        word = input("Word to insert: ")
        if word in dictionary.keys():  # Kollar om ordet matchar en av nycklarna i dictionary
            print("Error: Word already exists!")
        else:  # Lägget till ordet och förklaringen i dictionary
            desc = input("Description of word: ")
            dictionary.update({word: desc})

    def lookup_dic2():  # Anropas om användaren väljer att söka efter ett ord (Val 2)
        search = input("Word to lookup: ")
        if search not in dictionary.keys():
            print("Error: Word does not exist!")
        else:
            print("Description for", search, ":", dictionary[search])

    def delete_dic2():  # Anropas om användaren väljer att bort ett ord (Val 3)
        word = input("Word to delete: ")
        if word not in dictionary.keys():  # Kollar om ordet inte finns i dictionary
            print("Error: Word does not exist!")
        else:  # Tar bort ordet och förklaringen från dictionary
            dictionary.pop(word)
            print(word, "was sucessfully deleted.")

    menu(insert_dic2, lookup_dic2, delete_dic2)


#---------ORDLISTA MED TUPLER---------#


def main_dic3():  # Huvudfunktionen för tuple versionen av programmet

    tupleList = []

    def insert_dic3():  # Anropas om användaren väljer att lägga till ett ord (Val 1)
        word = input("Word to insert: ")
        if isInList(word):  # Kollar om ordet redan finns i listan med funktionen isInList()
            print("Error: Word already exists!")
        else:  # Lägger till ordet och förklaringen om ordet inte finns i listan
            desc = input("Description of word: ")
            tupleList.append((word, desc))

    def lookup_dic3():  # Anropas om användaren väljer att söka efter ett ord (Val 2)
        search = input("Word to lookup: ")
        if not isInList(search):  # Kollar om ordet inte finns i listan med funktionen isInList()
            print("Error: Word does not exist!")
        else:  # Söker igenom listan och om x[0] alltså något av orden matchar det sökta ordet skrivs ordet x[0] och den matchande förklaringen x[1] ut
            for x in tupleList:
                if x[0] == search:
                    print("Description for", x[0], ":", x[1])

    def delete_dic3():  # Anropas om användaren väljer att bort ett ord (Val 3)
        word = input("Word to delete: ")
        if not isInList(word):  # Kollar om ordet inte finns i listan med funktionen isInList()
            print("Error: Word does not exist!")
        else:  # Söker igenom listan och tar bort hela tuplen med ordet och förklaringen i
            for x in tupleList:
                if x[0] == word:
                    tupleList.pop(tupleList.index((x[0], x[1])))
                    print(x[0], "was successfully deleted.")


    def isInList(word):  # Funktion för att söka igenom listan. Returnerar True om ordet finns och False om det inte gör det
        for x in tupleList:
            if x[0] == word:
                return True
        return False

    menu(insert_dic3, lookup_dic3, delete_dic3)
