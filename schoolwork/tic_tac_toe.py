grid = [                #list of lists
    [" ", " ", " "],    #row 0
    [" ", " ", " "],    #row 1
    [" ", " ", " "],    #row 2
]

def display_grid():
    print()
    print("+---+---+---+")
    for row in grid:
        print(f"| {" | ".join(row)} |")
        print("+---+---+---+")

def assign_mark(turn):
    if turn % 2 == 1:
        return "X"
    else:
        return "O"
    
def get_player_move():
    while True:
        row = int(input("Pick a row (1, 2, 3)"))
        if row < 1 or row > 3:
            print("Invalid row number -- Try again.")
            continue
        column = int(input("Pick a column (1, 2, 3)"))
        if column < 1 or column > 3:
            print("Invalid row number -- Try again.")
            continue
        if not grid[row-1][column - 1] == " ":
            print("This square is already taken.")
            continue
        return row, column
    
def check_for_winner():
    #rows
    for x in range(3):
        if grid[x][0] == grid [x][1] and grid[x][1] == grid[x][2]:
            return grid[x][0]
    #columns
    for y in range(3):
        if grid[0][y] == grid [1][y] and grid[1][y] == grid[2][y]:
            return grid[0][y]
    #diag 1
    if grid[0][0] == grid [1][1] and grid[1][1] == grid[2][2]:
            return grid[0][0]
    #diag 2
    if grid[0][2] == grid [1][1] and grid[1][1] == grid[2][0]:
            return grid[0][2]
    #no winner
    return None

def is_game_over():
    turn = 1
    while True:
        mark = assign_mark(turn)
        print(f"{mark}'s turn")
        row, column = get_player_move()
        grid[row-1][column-1] = mark
        display_grid()
        winner=check_for_winner()
        
        if winner == "X" or winner == "O":
            print(f"\n{winner} wins!")
            game_over = True
            return game_over
        
        if turn == 9:
            print("It's a tie!")
            game_over = True
            return game_over
        print()

        if winner != "X" and winner != "O":
            print(f"No winner yet, play on!\n")

        turn += 1

def main():
    print("Welcome to Tic Tac Toe")
    display_grid()
    game_over = False
    while not game_over:
        game_over = is_game_over()
    print()
    print("Game over!")

if __name__ == "__main__":
    main()
