import os

board = [
    [" ", " "," "],
    [" ", " "," "],
    [" ", " "," "]
]

plays = 0
thatsAWin = False
isgameFinished = False

resetScreen = lambda: os.system("cls||clear")

def main():
    while not isgameFinished:
        DrawGame()
        InputPlayer()
        resetScreen()
    
    print("Finished game!")

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


def InputPlayer():
    global board, plays, isgameFinished

    if plays >= 2 and not thatsAWin:
        isgameFinished = True
    else: 
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
            
# Game function
main()