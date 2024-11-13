# let's make a text based tic-tac-toe game

# for now we will just show the board and ask for input

# we will need to keep track of the board state
# we will need to keep track of the current player

# we will need to check if the game is over

# we will need to check if the game is a draw
# we will need to check if the game is won

# so let's make a function to check if the game is over
# if the game is over we will return True

# let's make a function to check if the game is a draw

# let's make a function to check if the game is won

# board will be a two dimensional list of strings
# so list that has lists of strings of X, O, or empty string

# let's make a function to print the board
def print_board(board):
    for row in board:
        print(row)

# let's check if game is won
def is_game_won(board):
    # we will check if we have 3 in a row
    # first we will check if we have 3 in a row horizontally
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "":
            return True
    # then we will check if we have 3 in a row vertically
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "":
            return True
    # then we will check if we have 3 in a row diagonally
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return True
    return False

# let's make a function to check if the game is a draw
def is_game_draw(board):
    # if the board is full and no one has won then it's a draw
    for row in board:
        if "" in row:
            return False
    return True


# let's make a function to check if the game is over
def is_game_over(board):
    # if the game is over we will return True
    # game is over when we have 3 in a row or game board is full and it's a draw
    # so we will check if the game is won or if the game is a draw
    if is_game_won(board) or is_game_draw(board):
        return True
    # if the game is not over we will return False
    return False

# let's make a function to play the game
def play_the_game():
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    current_player = "X"
    while not is_game_over(board):
        print_board(board)
        try:
            row = int(input("Enter row: "))
            col = int(input("Enter col: "))
        except ValueError:
            print("Invalid input Enter Integer")
            continue
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid move")
            print("Valid moves are 0, 1, 2 for row and col")
            continue
        # check if move is valid and not already taken
        if board[row][col] != "":
            print("Invalid move")
            continue
        
        board[row][col] = current_player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    # game is over we want to know who won or if it's a draw
    print_board(board)
    if is_game_won(board):
        if current_player == "X":
            print("O won")
        else:
            print("X won")
    else:
        print("It's a draw")

# let's make a main function
def main():
    print("Welcome to Tic Tac Toe")
    play_the_game()
    print("Game Over")

# let's call the main function
# now someone could actually import this module and use the functions
if __name__ == "__main__":
    main()

# TODO
# possible improvements
# add a computer player
# add an option to play again
# could save the game state to a file or sqlite database
# could display game on tk or web or pygame