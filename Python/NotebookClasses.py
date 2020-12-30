import time
import os


class Library:
    """Maintains which notebook is in use and finds the notebooks in dir"""
    def __init__(self):
        self.bookName = "Untitled"
        self.noteBook = Notebook()

    def getName(self):
        """Returns name of current notebook"""
        return self.bookName

    def showBooks(self):
        """Lists all .txt files in dir"""
        listOfBooks = []
        for file in os.listdir("."):
            if file.endswith(".txt"):
                listOfBooks.append(os.path.join(file))
        return listOfBooks

    def getContent(self):
        """Returns content of notebook as list if lines"""
        content = []
        try:
            book = open(self.bookName, "r")
            content = book.read().splitlines()
            book.close()
            return content
        except FileNotFoundError:
            print("No notebook currently open.\n")
            return content

    def saveContent(self, content):
        """Checks if user wants to save into open notebook or into a new one"""
        if self.bookName.endswith(".txt"):
            while True:
                choice = input("\nDo you wish to save into current notebook? Y/N: ").lower()
                if choice == "y":
                    self.saver(content)
                    return
                elif choice == "n":
                    break
                else:
                    print("\nInvalid input")
                    continue
        self.bookName = input("\nPlease give name for new notebook: ")
        if not self.bookName.endswith(".txt"):  # Makes sure the filename ends with.txt
            self.bookName = self.bookName + ".txt"
        self.saver(content)

    def saver(self, content):
        """Saves list of notes to notebook"""
        book = open(self.bookName, "w+")
        for element in content:
            book.write(element)
            book.write("\n")
        book.close()
        print("\nNotes saved to notebook.\n")

    def changeBook(self):
        listOfBooks = self.showBooks()
        if not listOfBooks:
            print("No .txt files found in dir.\n")
            return
        else:
            print(listOfBooks)
            newBook = input("\nWhich notebook should we open? ")
            if not newBook.endswith(".txt"):  # Makes sure the filename ends with.txt
                newBook = newBook + ".txt"
            if newBook in listOfBooks:
                self.bookName = newBook
                print("Opened: ", newBook)
                self.noteBook.newContent(self.getContent())
            else:
                print("Notebook not found.\n")
                return


class Notebook:
    """Reads, writes and edits content of notebook"""
    def __init__(self):
        self.content = []

    def newContent(self, newLines):
        self.content = newLines

    def lineTester(self):
        """Tests whether the line number is present in the list"""
        print("The list has", len(self.content), "notes.\n")
        while True:
            try:
                lineNumber = int(input("Give number of line to edit: "))
            except ValueError:
                print("Incorrect choice, please select a number.\n")
                continue
            try:
                lineNumber -= 1
                print("Note: ", self.content[lineNumber])
                return lineNumber
            except IndexError:
                print("no such line in notebook.\n")
                continue

    def getLine(self):
        """Gets line from list"""
        return self.content[self.lineTester()]

    def replaceLine(self):
        """Replaces line in list with new one"""
        print("Replacing: ")
        lineToReplace = self.lineTester()
        newLine = input("Write new note: ")
        self.content[lineToReplace] = newLine + " ::: " + time.strftime("%X %x")

    def deleteLine(self):
        """Deletes existing line"""
        print("Deleting: ")
        toDelete = self.lineTester()
        del self.content[toDelete]

    def appendList(self, newLine):
        """Appends new line into list"""
        self.content.append(newLine)

    def printContent(self):
        """prints amount of notes and the contents of the list of notes"""
        print("The list has", len(self.content), "notes.\n")
        print(*self.content, sep="\n")

    def createLine(self):
        """Creates new line with timestamp"""
        newLine = input("\nWrite a new note: ")
        print("New note: " + newLine + " ::: " + time.strftime("%X %x\n"))
        self.content.append(newLine + " ::: " + time.strftime("%X %x"))


class UserInterface:
    """Instantiates all classes"""
    def __init__(self):
        self.openBook = Library()

    def printContent(self):  # Prints out content of notebook.
        self.openBook.noteBook.printContent()
        self.Chooser()

    def createLine(self):  # Adds a new note to the notebook with a timestamp.
        self.openBook.noteBook.createLine()
        self.Chooser()

    def replaceLine(self):  # Prints out and deletes selected note,
        # expects new input to replace deleted note.
        self.openBook.noteBook.replaceLine()
        self.Chooser()

    def deleteLine(self):  # Deletes selected note.
        self.openBook.noteBook.deleteLine()
        self.Chooser()

    def changeBook(self):  # Changes Notebook, creates new one if name not found.
        self.openBook.changeBook()
        self.Chooser()

    def saveContent(self):  # Saves all changes made to notebook
        self.openBook.saveContent(self.openBook.noteBook.content)
        self.Chooser()

    def Exit(self):  # Exits program.
        print("Notebook shutting down.\nThank you for your patronage.")

    def default(self):
        print("\nInvalid choice\n")
        self.Chooser()

    def Chooser(self):
        """Allows user to choose actions"""
        print("\nCurrent notebook: ", self.openBook.bookName)
        print("\n(1) Read the notebook\n(2) Add note\n(3) Edit a note\n(4) Delete a note\n"
              "(5) Change notebook\n(6) Save notes to notebook\n(7) Quit(remember to save)\n")
        options = {
            1: self.printContent,
            2: self.createLine,
            3: self.replaceLine,
            4: self.deleteLine,
            5: self.changeBook,
            6: self.saveContent,
            7: self.Exit,
        }
        try:
            choice = int(input("Please select action: "))
            options.get(choice, self.default)()
        except ValueError:
            print("\nInvalid choice\n")
            self.Chooser()


if __name__ == '__main__':
    user = UserInterface()
    user.Chooser()
