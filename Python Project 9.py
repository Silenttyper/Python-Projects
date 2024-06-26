#TicTacToe Game
import random

print("Welcome To TicTacToe Game")
print("-------------------------")

possiblenumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gameboard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = 3
cols = 3

def PrintGameBoard():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(cols):
            print("", gameboard[x][y], end=" | ")
    print("\n+---+---+---+")

# Function to modify the gameboard array
def ModifyArray(num, turn):
    # The index number for this goes like this. The first number is the row and the 2nd number is the column
    num -= 1  # Do this so you start at 0
    if num == 0:
        gameboard[0][0] = turn
    elif num == 1:
        gameboard[0][1] = turn
    elif num == 2:
        gameboard[0][2] = turn
    elif num == 3:
        gameboard[1][0] = turn
    elif num == 4:
        gameboard[1][1] = turn
    elif num == 5:
        gameboard[1][2] = turn
    elif num == 6:
        gameboard[2][0] = turn
    elif num == 7:
        gameboard[2][1] = turn
    elif num == 8:
        gameboard[2][2] = turn

# Function to check for a winner
def CheckForWinner(gameBoard):
    # X axis
    for row in gameBoard:
        if row[0] == row[1] == row[2]:
            return row[0]

    # Y axis
    for col in range(3):
        if gameBoard[0][col] == gameBoard[1][col] == gameBoard[2][col]:
            return gameBoard[0][col]

    # Cross wins/diagonal win
    if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2]:
        return gameBoard[0][0]
    if gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0]:
        return gameBoard[0][2]

    return None

LeaveLoop = False
turnCounter = 0  # Keeps track of if it is my turn or the computer's turn

PrintGameBoard()  # Print the initial board with all numbers

while not LeaveLoop:
    # It's the player's turn
    if turnCounter % 2 == 0:
        numberPicked = int(input("\nChoose a number [1-9]: "))
        # Validate the number picked by the user
        if 1 <= numberPicked <= 9 and numberPicked in possiblenumbers:
            ModifyArray(numberPicked, "X")
            possiblenumbers.remove(numberPicked)
            turnCounter += 1
            PrintGameBoard()  # Print the updated board after the player's move
        else:
            print("Invalid input. Please try again.")
    else:
        # The computer's turn
        CPUChoice = random.choice(possiblenumbers)
        print("\nCPU Choice: ", CPUChoice)
        ModifyArray(CPUChoice, "O")
        possiblenumbers.remove(CPUChoice)
        turnCounter += 1
        PrintGameBoard()  # Print the updated board after the computer's move

    # Check for a winner or a tie
    winner = CheckForWinner(gameboard)
    if winner:
        print(f"{winner.upper()} has won the game!")
        LeaveLoop = True
    elif not possiblenumbers:
        print("It's a tie!")
        LeaveLoop = True
