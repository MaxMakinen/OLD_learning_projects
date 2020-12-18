import time
import pickle


def newbook(name): # For changing notebook, or creating a new notebook
    try:
        book = open(name, "rb")
        book.close()
    except IOError:
        book = open(name, "wb")
        print("No notebook with that name detected, created one.")
        book.close()


read = []
name = "notebook.dat"
try:
    book = open("notebook.dat", "rb") # Attempting to open notebook, creates a new one if none found
    read = pickle.load(book)
    book.close()
except IOError:
    book = open("notebook.dat", "wb")
    print("No default notebook was found, created one.")
    book.close()

while True:
    print("\n(1) Read the notebook\n(2) Add note\n(3) Edit a note\n(4) Delete a note\n(5) Save and quit\n")
    try:
        choice = int(input("Please select one: "))
    except Exception:
        continue
    if choice == 1: # Prints out content of notebook
        for i in read:
            print(i)
    elif choice == 2: # Adds a new note to the notebook with a timestamp
        stuff = input("Write a new note: ")
        read.append(stuff + ":::" + time.strftime("%X %x"))
    elif choice == 3: # Prints out and then deletes selected note, excpetcs new input to replace deleted note
        try:
            print("The list has", len(read), "notes.")
            edit = int(input("Which of them will be changed?: "))
            print(read.pop(edit - 1))
            read.insert(edit, input("Give the new note: ") + ":::" + time.strftime("%X %x"))
        except Exception:
            continue
    elif choice == 4: # Deletes selected note
        try:
            print("The list has", len(read), "notes.")
            edit = int(input("Which of them will be deleted?: "))
            print("Deleted note", read.pop(edit - 1))
        except Exception:
            continue
    elif choice == 5: # Saves all changes made to notebook and then exits program
        book = open("notebook.dat", "wb")
        pickle.dump(read, book)
        book.close()
        print("Notebook shutting down, thank you.")
        
        break
