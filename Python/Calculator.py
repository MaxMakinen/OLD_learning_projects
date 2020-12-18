import math
def givenum():
    while True:
        try:
            num = int(input("Give a number: "))
            return num
        except ValueError:
            print("This input is invalid.")

print("Calculator.\nThis calculator asks for two numbers, then it will request an operator")
first = givenum()
second = givenum()
while True:
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2)\n(6)cos(number1/number2)\n(7)Change numbers\n(8)Quit\nCurrent numbers:", first, second)
    choice = int(input("Please select something (1-6): "))
    if choice == 1:
        print("\nThe result is:", first + second,"\n")
    elif choice == 2:
        print("\nThe result is:", first - second,"\n")
    elif choice == 3:
        print("\nThe result is:", first * second,"\n")
    elif choice == 4:
        print("\nThe result is:", first / second,"\n")
    elif choice == 5:
        print("\nThe result is:", math.sin((first/second)),"\n")
    elif choice == 6:
        print("\nThe result is:", math.cos((first/second)),"\n")
    elif choice == 7:
        first = int(input("Give the first number: "))
        second = int(input("Give the second number: "))
    elif choice == 8:
        print("Thank you!")
        break
