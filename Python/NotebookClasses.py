import time

class Library:
    '''Maintains which notebook is in use, if none found, creates new one'''
    def __init__(self, name):
        self.bookName = name
        try:
            book = open(self.bookName, "r")
            book.close()
        except IOError:
            book = open(self.bookName, "w")
            print("No notebook with that name detected, created one.")
            book.close()

    def getName(self):
        '''Returns name of opened notebook'''
        return self.bookName

    def getContent(self):
        '''Returns content of notebook as list if lines'''
        book = open(self.bookName, "r")
        content = book.read().splitlines()
        book.close()
        return content

    def saveContent(self, content):
        '''Saves list of notes to notebook'''
        book = open(self.bookName, "w")
        for element in content:
            book.write(element)
            book.write("\n")
        book.close()


class Notebook:
    '''Reads, writes and edits content of notebook'''
    def __init__(self, openedBook):
        self.content = openedBook.getContent()

    def lineTester(self):
        '''Tests whether the line number is present in the list'''
        print("The list has", len(self.content), "notes.")
        while True:
            try:
                lineNumber = int(input("Give number of line to edit: "))
            except ValueError:
                print("Incorrect choice, please select a number")
                continue
            try:
                lineNumber -= 1
                print("Note: ", self.content[lineNumber])
                return lineNumber
            except IndexError:
                print("no such line in notebook")
                continue


    def getLine(self):
        '''Gets line from list'''
        try:
            return self.content[self.lineTester()]
        except TypeError:
            return False

    def replaceLine(self):
        '''Replaces line in list with new one'''
        print("Replacing: ")
        try:
            lineToReplace = self.lineTester()
        except TypeError:
            return False
        newLine = input("Write new note: ")
        self.content[lineToReplace] = newLine +  " ::: " + time.strftime("%X %x")

    def deleteLine(self):
        '''Deletes existing line'''
        print("Deleting: ")
        try:
            toDelete = self.lineTester()
        except TypeError:
            return
        del self.content[toDelete]

    def appendList(self, newLine):
        '''Appends new line into list'''
        self.content.append(newLine)

    def printContent(self):
        '''prints amount of notes and the contents of the list of notes'''
        theList = self.content
        print("The list has", len(theList), "notes.")
        print(theList)


class Note:
    '''Manages individual lines and timestamps for writing.'''
    def __init__(self, noteBook):
        self.noteBook = noteBook

    def createLine(self):
        '''Creates new line with timestamp'''
        newLine = input("Write a new note: ")
        print ("New note: " + newLine + " ::: " + time.strftime("%X %x"))
        return newLine + " ::: " + time.strftime("%X %x")


class userInterface:
    '''Instantializes all classes'''
    def __init__(self):
        self.openBook = Library("Notebook.txt")
        self.noteBook = Notebook(self.openBook)
        self.note = Note(self.noteBook)

    def Chooser(self):
        '''Allows user to choose actions'''
        while True:
            print("Current notebook: ", self.openBook.getName())
            print("\n(1) Read the notebook\n(2) Add note\n(3) Edit a note\n(4) Delete a note\n"
                  "(5) Change notebook\n(6) Save notes to notebook\n(7) Quit(Remember to save)\n")
            try:
                choice = int(input("Please select one: "))
                if choice == 1:  # Prints out content of notebook.
                    self.noteBook.printContent()

                elif choice == 2:  # Adds a new note to the notebook with a timestamp.
                    Line = self.note.createLine()
                    self.noteBook.appendList(Line)

                elif choice == 3:  # Prints out and then deletes selected note, expects new input to replace deleted note.
                    self.noteBook.replaceLine()

                elif choice == 4:  # Deletes selected note.
                    self.noteBook.deleteLine()

                elif choice == 5:  # Changes Notebook, creates new one if name not found.
                    newName = input("Give name of new notebook: ")
                    self.openBook = Library(newName)
                    self.noteBook = Notebook(self.openBook)

                elif choice == 6: # Saves all changes made to notebook3
                    self.openBook.saveContent(self.noteBook.content)
                    print("Notes saved to notebook")

                elif choice == 7:  # Exits program.
                    print("Notebook shutting down,\nthank you for your patronage.")
                    break
                else:
                    print("Incorrect choice")
                    continue
            except ValueError:
                print("Incorrect choice")


if __name__ == '__main__':
    userI = userInterface()
    userI.Chooser()
