import os 
import random

# Game board
board = [
    [" ", " "," "],
    [" ", " "," "],
    [" ", " "," "]
]
# Game variables
plays = 0
thatsAWin = False
isgameFinished = False
winner = ""

# Game functions
resetScreen = lambda: os.system("cls||clear")

# Main function
def main():
    global plays, isgameFinished, winner

    while not isgameFinished:
        DrawGame()
        if plays >= 9 or thatsAWin:
            isgameFinished = True
        else:
            InputPlayer()
            InputCPU()
            resetScreen()
    
    print("Finished game!")
    if thatsAWin:
        print(f"{winner} wons the game!")

# Function that draws the game
def DrawGame():
    global plays

    # Draw the game board
    print("  0   1   2")
    print(f"0 {board[0][0]} | {board[0][1]} | {board[0][2]}  ")
    print("  ----------")
    print(f"1 {board[1][0]} | {board[1][1]} | {board[1][2]}  ")
    print("  ----------")
    print(f"2 {board[2][0]} | {board[2][1]} | {board[2][2]}  ")
    print("\nPlays:" + str(plays))

# Receive player input
def InputPlayer():
    global board, plays

    try:
        row = int(input("Enter row:"))
        col = int(input("Enter column:"))
    except:
        print("Invalid input!")
        InputPlayer()
    else:
        if row < len(board):
            if col < len(board[row]):
                if board[row][col] == " ":
                    board[row][col] = "x"
                    plays += 1
                else:
                    print("Look for another spot!")
                    InputPlayer()
    
    WinChecker("x")
                    
# CPU decisions
def InputCPU():
    global board, plays, winner

    row = random.randint(0,2)
    col = random.randint(0,2)

    if board[col] != "x":
        board[row][col] = "o"
        plays += 1
        WinChecker("o")
    else:
        row = random.randint(0,2)
        col = random.randint(0,2)
    
def WinChecker(who):
    global board, thatsAWin, winner

    # Check rows
    for row in board:
        if row.count(who) == 3:
            thatsAWin = True
            winner = "CPU(o)" if who == "o" else "Player(x)"
            return

    # Check columns
    for col in range(3):
        if board[0][col] == who and board[1][col] == who and board[2][col] == who:
            thatsAWin = True
            winner = "CPU(o)" if who == "o" else "Player(x)"
            return

    # Check diagonals
    if board[0][0] == who and board[1][1] == who and board[2][2] == who:
        thatsAWin = True
        winner = "CPU(o)" if who == "o" else "Player(x)"
        return
    if board[0][2] == who and board[1][1] == who and board[2][0] == who:
        thatsAWin = True
        winner = "CPU(o)" if who == "o" else "Player(x)"
        return
 
# Runnner
main()

# --- Imacod3r --- #