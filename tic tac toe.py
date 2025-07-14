import random

print("Let's play Tic Tac Toe.\nChoose mode:")
print("1. Multiplayer")
print("2. Play with Computer")

mode = input("Enter 1 or 2: ")

arr = [["__|", "__", "|__"],
       ["__|", "__", "|__"],
       ["__|", "__", "|__"]]

arr1 = [["00", "01", "02"],
        ["10", "11", "12"],
        ["20", "21", "22"]]

def show_board():
    for row in arr:
        print("".join(row))

def mark_position(choice, symbol):
    if choice == "00":
        arr1[0][0] = symbol
        arr[0][0] = f" {symbol} |"
    elif choice == "01":
        arr1[0][1] = symbol
        arr[0][1] = f" {symbol} "
    elif choice == "02":
        arr1[0][2] = symbol
        arr[0][2] = f" |{symbol} "
    elif choice == "10":
        arr1[1][0] = symbol
        arr[1][0] = f" {symbol} |"
    elif choice == "11":
        arr1[1][1] = symbol
        arr[1][1] = f" {symbol} "
    elif choice == "12":
        arr1[1][2] = symbol
        arr[1][2] = f" |{symbol} "
    elif choice == "20":
        arr1[2][0] = symbol
        arr[2][0] = f" {symbol} |"
    elif choice == "21":
        arr1[2][1] = symbol
        arr[2][1] = f" {symbol} "
    elif choice == "22":
        arr1[2][2] = symbol
        arr[2][2] = f" |{symbol} "
    show_board()

def first_chance():
    print("Enter the choice of 1st player\n")
    choice = input()
    while choice not in [cell for row in arr1 for cell in row]:
        print("Invalid or already taken spot. Try again:")
        choice = input()
    mark_position(choice, "X")

def second_chance():
    print("Enter the choice of 2nd player\n")
    choice = input()
    while choice not in [cell for row in arr1 for cell in row]:
        print("Invalid or already taken spot. Try again:")
        choice = input()
    mark_position(choice, "O")

def computer_chance():
    print("Computer's turn\n")
    available = [cell for row in arr1 for cell in row if cell not in ["X", "O"]]
    choice = random.choice(available)
    print("Computer chose", choice)
    mark_position(choice, "O")

def win_chance():
    w = [[arr[0][0], arr[0][1], arr[0][2]],
         [arr[1][0], arr[1][1], arr[1][2]],
         [arr[2][0], arr[2][1], arr[2][2]],
         [arr[0][0], arr[1][0], arr[2][0]],
         [arr[0][1], arr[1][1], arr[2][1]],
         [arr[0][2], arr[1][2], arr[2][2]],
         [arr[0][0], arr[1][1], arr[2][2]],
         [arr[0][2], arr[1][1], arr[2][0]]]
    for line in w:
        if line.count(" X ") == 3 or line.count(" X |") == 3 or line.count("|X ") == 3:
            print("Player 1 Wins")
            exit()
        if line.count(" O ") == 3 or line.count(" O |") == 3 or line.count("|O ") == 3:
            if mode == "1":
                print("Player 2 Wins")
            else:
                print("Computer Wins")
            exit()
    if all(cell in ["X", "O"] for row in arr1 for cell in row):
        print("Draw")
        exit()

def multiplayer():
    show_board()
    for _ in range(5):
        first_chance()
        win_chance()
        if _ == 4:
            break
        second_chance()
        win_chance()

def with_computer():
    show_board()
    for _ in range(5):
        first_chance()
        win_chance()
        if _ == 4:
            break
        computer_chance()
        win_chance()

if mode == "1":
    multiplayer()
elif mode == "2":
    with_computer()
else:
    print("Invalid input. Restart the program.")
