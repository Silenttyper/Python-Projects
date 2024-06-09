#Tic Tac Toe Game 
import random

print("Welcone To TicTacToe Game")
print("-------------------------")


possiblenumbers=[1,2,3,4,5,6,7,8,9]
gameboard=[[1,2,3], [4,5,6],[7,8,9]]
rows=3
cols=3

def PrintGameBoard():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(cols):
            print("", gameboard[x][y], end=" | ")
    print("\n+---+---+---+")
PrintGameBoard()

def ModifyArray(num,turn):
    #The index number for this goes like this. The first number is the row and the 2nd number is the column
    num-=1 #Do this so you start at 0
    if (num==0):
        gameboard[0][0] = turn
    elif (num==1):
        gameboard[0][1] = turn
    elif (num==2):
        gameboard[0][2] = turn
    elif(num==3):
        gameboard[1][0] = turn
    elif(num==4):
        gameboard[1][1] = turn
    elif(num==5):
        gameboard[1][2] = turn
    elif (num==6):
        gameboard[2][0] = turn
    elif (num==7):
        gameboard[2][1] = turn
    elif (num==9):
        gameboard[2][2] = turn

def CheckForWinner(gameBoard):
    #X acis
    if gameBoard[0][0] =="x" and gameBoard[0][1]=="x" and gameBoard[0][2]=="x":
        print("X has won the game")
        return "x"
    elif gameBoard[0][0] =="o" and gameBoard[0][1]=="o" and gameBoard[0][2]=="o":
        print("X has won the game")
        return "o"
    #Y axis
    elif gameBoard[0][0] =="x" and gameBoard[1][0]=="x" and gameBoard[2][0]=="x":
        print("X has won")
        return "x"
    
    elif gameBoard[0][0] =="o" and gameBoard[1][0]=="o" and gameBoard[2][0]=="o":
        print("O has won")
        return "o"
    #Cross wins/diaganol win
    elif gameBoard[0][0]=="x" and gameBoard[1][1]=="x" and gameBoard[2][2]=="x":
        print("X has won")
        return "x"
    
    elif gameBoard[0][0]=="o" and gameBoard[1][1]=="o" and gameBoard[2][2]=="o":
        print("O has won")
        return "o"

LeaveLoop= False
turnCounter=0 #Keeps track of if it is my turn or the computers turn
while (LeaveLoop==False):
    #Its the players turn
    if (turnCounter % 2==1):
        PrintGameBoard
        numberPicked=int(input("\nChoose a number [1-9: ] "))
        if(numberPicked >= 1 or numberPicked <=9):
            ModifyArray(numberPicked,"x")
            possiblenumbers.remove(numberPicked)
        else:
            print("Invalid input. Please try again. ")
        turnCounter+=1
        #Validate the number picked by the user
    #The computers turn
    else:
        while (True):
            CPUChoice=random.choice(possiblenumbers)
            print("\nCPU Choice: ", CPUChoice)
            if(CPUChoice in possiblenumbers):
                ModifyArray(CPUChoice, "o")
                possiblenumbers.remove(CPUChoice) #Remove the number the cpu just chose
                turnCounter+=1
                break
        

    

import random

print("Welcome To TicTacToe Game")
print("-------------------------")

possiblenumbers = [1,2,3,4,5,6,7,8,9]
gameboard = [[1,2,3], [4,5,6],[7,8,9]]
rows = 3
cols = 3

def PrintGameBoard():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(cols):
            print("", gameboard[x][y], end=" | ")
    print("\n+---+---+---+")
PrintGameBoard()

def ModifyArray(num, turn):
     #The index number for this goes like this. The first number is the row and the 2nd number is the column
    num -= 1#Do this so you start at 0
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

def CheckForWinner(gameBoard):
    #X acis
    for row in gameBoard:
        if row[0] == row[1] and row[1] == row[2]:
            return row[0]

    #Y axis
    for col in range(3):
        if gameBoard[0][col] == gameBoard[1][col] and gameBoard[1][col] == gameBoard[2][col]:
            return gameBoard[0][col]

    #Cross wins/diaganol win
    if gameBoard[0][0] == gameBoard[1][1] and gameBoard[1][1] == gameBoard[2][2]:
        return gameBoard[0][0]
    if gameBoard[0][2] == gameBoard[1][1] and gameBoard[1][1] == gameBoard[2][0]:
        return gameBoard[0][2]

    return None

LeaveLoop = False
turnCounter = 0#Keeps track of if it is my turn or the computers turn
while not LeaveLoop:
    #Its the players turn
    PrintGameBoard()
    if turnCounter % 2 == 1:
        numberPicked = int(input("\nChoose a number [1-9]: "))
        if 1 <= numberPicked <= 9 and numberPicked in possiblenumbers:
            ModifyArray(numberPicked, "x")
            possiblenumbers.remove(numberPicked)
            turnCounter += 1
             #Validate the number picked by the user
    #The computers turn
        else:
            print("Invalid input. Please try again.")
    else:
        CPUChoice = random.choice(possiblenumbers)
        print("\nCPU Choice: ", CPUChoice)
        ModifyArray(CPUChoice, "o")
        possiblenumbers.remove(CPUChoice)#Remove the number the cpu just chose
        turnCounter += 1
    
    winner = CheckForWinner(gameboard)
    if winner:
        PrintGameBoard()
        print(f"{winner.upper()} has won the game!")
        LeaveLoop = True

    if not possiblenumbers:
        PrintGameBoard()
        print("It's a tie!")
        LeaveLoop = True
