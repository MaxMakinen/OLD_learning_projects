import random



def main():
    played = 0
    wins = 0
    ties = 0
    while True:
        choice =input("Foot, Nuke or Cockroach? (Quit ends): ")
        comp = random.randint(1,3)		
        if choice == "Quit" or "quit": break
        if choice == "Foot" or "foot":
            print("You chose:",choice)
            if comp == 1:
                print("Computer chose: Foot")
                print("It is a tie!")
                ties += 1
                played += 1
                continue
            elif comp == 2:
                print("Computer chose: Nuke")
                print("You lose!")
                played += 1
                continue
            elif comp == 3:
                print("Computer chose: Cockroach")
                print("You Win!")
                wins += 1
                played += 1
                continue
        elif choice == "Nuke" or "nuke":
            print("You chose:",choice)
            if comp == 1:
                print("Computer chose: Foot")
                print("You Win!")
                wins += 1
                played += 1
                continue
            elif comp == 2:
                print("Computer chose: Nuke")
                print("Both lose!")
                played += 1
                continue
            elif comp == 3:
                print("Computer chose: Cockroach")
                print("You lose!")
                played += 1
                continue
        elif choice == "Cockroach" or "cockroach":
            print("You chose:",choice)
            if comp == 1:
                print("Computer chose: Foot")
                print("You lose!")
                played += 1
                continue
            elif comp == 2:
                print("Computer chose: Nuke")
                print("You Win!")
                wins += 1
                played += 1
                continue
            elif comp == 3:
                print("Computer chose: Cockroach")
                print("It is a tie!")
                ties += 1
                played += 1
                continue
        else:
            print("Incorrect selection.")
            continue
    print("You played", played, "rounds, and won", wins, "rounds, playing tie in", ties, "rounds.")
if __name__ == "__main__":
	main()
