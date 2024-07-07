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

# Game functions
resetScreen = lambda: os.system("cls||clear")

# Main function
def main():
    global plays, isgameFinished

    while not isgameFinished:
        DrawGame()
        if plays >= 9 and not thatsAWin:
            isgameFinished = True
        else:
            InputPlayer()
            InputCPU()

        resetScreen()
    
    print("Finished game!")

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
                board[row][col] = "x"
                plays += 1

# CPU decisions
def InputCPU():
    global board, plays

    row = random.randint(0,2)
    col = random.randint(0,2)

    if board[col] != " ":
        board[row][col] = "o"
        plays += 1
    else:
        InputCPU()
    


            
# Run function
main()