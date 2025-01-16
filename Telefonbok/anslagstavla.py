class Board:
    def __init__(self, msg):
        self.message = msg

    def postMessage(self, msg : str):
        self.message += " " + msg

    def getMessage(self):
        return self.message


def main():
    
    # Returns the board that the (person) dosen't have
    def getOppositeBoard(person : Board):
        if person == board1:
            return board2
        return board1

    running = True

    board1 = Board("")
    board2 = Board("")

    kim = board1
    chris = board2
  
    # Menu loop stops when user chooses option 0
    while running:
        print("=== Bulletin board system ===")
        print("Kim reads message: " + kim.getMessage())
        print("Chris reads message: " + chris.getMessage())
        print("1: Direct Kim to other board")
        print("2: Direct Chris to other board")
        print("3: Tell Kim to post a message")
        print("4: Tell Chris to post a message")
        print("0: Exit")
        
        option = int(input("Enter choice: "))

        if option == 1:
            kim = getOppositeBoard(kim)
        elif option == 2:
            chris = getOppositeBoard(chris)
        elif option == 3:
            kim.postMessage(input("Enter message: "))
        elif option == 4:
            chris.postMessage(input("Enter message: "))
        elif option == 0:
            running = False
        else:
            print("Enter a valid option!")

main()