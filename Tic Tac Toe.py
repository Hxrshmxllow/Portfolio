import random

gameboard = [['   ','   ','   '], 
             ['   ','   ','   '], 
             ['   ','   ','   ']]

def printboard():
    print("-_-| 1 | 2 | 3 ")
    print("---------------")
    for i in range(3):
        print(str(i + 1) + "  |" + gameboard[i][0] + "|" + gameboard[i][1] + "|" + gameboard[i][2])
        if i != 2:
            print("---|---|---|---")

def computer():
    availablecells = []
    #checks all 8 combinations (3rows, 3columns, 2diagonals)
    combinations = [0, 0, 0, 0, 0, 0, 0, 0] 
    for row in range(3):
        for column in range(3):
            if gameboard[row][column] == " X ":
                combinations[row] += 1
                combinations[column + 3] += 1
                if (row == 0 and column == 0) or (row == 1 and column == 1) or (row == 2 and column == 2):
                    combinations[6] += 1
                elif (row == 0 and column == 2) or (row == 1 and column == 1) or (row == 2 and column == 0):
                    combinations[7] += 1

            elif gameboard[row][column] == "   ":
                availablecells.append([row, column])
                 
    for i in range(8):
        if combinations[i] == 0 or combinations[i] < 3 and combinations[i] == 2:
            for cells in availablecells:
                 if cells[0] == i:
                    gameboard[cells[0]][cells[1]] = " O "
                    printboard()
                    return
        elif combinations[i] == 3 or combinations[i] < 6 and combinations[i] == 2:
            for cells in availablecells:
                 if cells[1] == i:
                    gameboard[cells[0]][cells[1]] = " O "
                    printboard()
                    return
        elif combinations[i] == 6 and combinations[i] == 2:
            for cells in availablecells:
                 if cells == [0,0] or cells == [1,1] or cells == [2,2]:
                    gameboard[cells[0]][cells[1]] = " O "
                    printboard()
                    return
        elif combinations[i] == 7 and combinations[i] == 2:
            for cells in availablecells:
                 if cells == [0,2] or cells == [1,1] or cells == [2,0]:
                    gameboard[cells[0]][cells[1]] = " O "
                    printboard()
                    return
                     
    cell = random.choice(availablecells)
    gameboard[cell[0]][cell[1]] = " O "
    printboard()
    return
              
def checkwin(player):
    drawcounter = 0
    for i in range(3):
        # Check rows
        if gameboard[i][0] == gameboard[i][1] == gameboard[i][2] == player:
            print("Player {} wins!".format(player))
            exit()
        # Check columns
        elif gameboard[0][i] == gameboard[1][i] == gameboard[2][i] == player:
            print("Player {} wins!".format(player))
            exit()
        # Checks every cell if its empty
        for j in range(3):
            if gameboard[i][j] != "   ":
                drawcounter += 1

    # Check diagonals
    if gameboard[0][0] == gameboard[1][1] == gameboard[2][2] == player:
        print("Player {} wins!".format(player))
        exit()
    elif gameboard[0][2] == gameboard[1][1] == gameboard[2][0] == player:
        print("Player {} wins!".format(player))
        exit()
    elif drawcounter == 9:
        print("Tie game!")
        exit()

def main():
    winner = False
    print("Welcome to Tic Tac Toe!")
    printboard()
    loop = True
    while loop == True:
        row = 0
        column = 0
        while (row > 3 or row <= 0):
                row = int(input("Enter the row number (1-3): "))
                if(row > 3 or row <= 0):
                    print("Please try a number between 0 and 3.")
        while (column > 3 or column <= 0):
            column = int(input("Enter the column number (1-3): ")) 
            if(column > 3 or column <= 0):
                    print("Please try a number between 0 and 3.")
        if gameboard[row - 1][column - 1] == "   ":
                gameboard[row - 1][column - 1] = " X "
                printboard()
                checkwin(" X ")
                computer()
                checkwin(" O ")
        else:
            print("Cannot place there. Try again!")
        

if __name__ == "__main__":
    main()