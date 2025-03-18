from tabulate import tabulate
import random

data = [["", "", ""], ["", "", ""], ["", "", ""]]

usrChoice = int(input("Enter your choice: ✔️(1) or ⭕(0): "))
cmpChoice = None

if usrChoice == 1:
    usrChoice = "✔️"
    cmpChoice = "⭕"
elif usrChoice == 0:
    usrChoice = "⭕"
    cmpChoice = "✔️"
else:
    print("Enter a valid choice: 1 or 0")

def table():
    print(tabulate(data, tablefmt="grid"))

def isCellEmpty(row, col):
    return data[row][col] == ""

def checkWin():
    for row in data:
        if row[0] == row[1] == row[2] != "":
            return row[0]
    for col in range(3):
        if data[0][col] == data[1][col] == data[2][col] != "":
            return data[0][col]
    if data[0][0] == data[1][1] == data[2][2] != "":
        return data[0][0]
    if data[0][2] == data[1][1] == data[2][0] != "":
        return data[0][2]
    return None

for turn in range(9):
    table()
    winner = checkWin()
    if winner:
        print(f"{winner} wins the game!")
        break

    if turn % 2 == 0:
        try:
            row = int(input("Enter the row number(0,1,2): "))
            col = int(input("Enter the column number(0,1,2): "))

            if isCellEmpty(row, col):
                data[row][col] = usrChoice
            else:
                print("Cell already occupied, try another one")
                continue
        except (ValueError, IndexError):
            print("Invalid input! enter row and column numbers between 0 and 2")
            continue
    else:
        print("Computer is making its move.")
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)

            if isCellEmpty(row, col):
                data[row][col] = cmpChoice
                break

else:
    table()
    print("It's a draw!")
