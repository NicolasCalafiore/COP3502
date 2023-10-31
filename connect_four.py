# Prints the current state of the board
def print_board(board):
    for i in reversed(board):
        for j in i:
            print(j, end = " ")
        print()

# Initializes the board with empty cells
def initialize_board(Height, Length):
    board = []
    for i in range(Height):
        board.append([])
        for j in range(Length):
            board[i].append("-")
    return board

# Inserts a chip in the selected column
def insert_chip(board, column, token):
    for i in range(len(board)):
        if board[i][column] == "-":
            board[i][column] = token
            return

    print("Invalid move")
    insert_chip(board, column, token)

# Checks if there are four consecutive chips of the same type in a list
def run_counter(lst, token):
    for i in range(len(lst)-3):
        if lst[i:i+4] == [token]*4:
            return True
    return False

# Checks if the current player has won
def check_if_winner(board, length, height, token):
    evaluation_list = []
    # Check horizontal wins
    for i in range(height):
        for j in range(length):
            evaluation_list.append(board[i][j])
        if run_counter(evaluation_list, token):
            return True
        evaluation_list = []
    # Check vertical wins
    for i in range(length):
        for j in range(height):
            evaluation_list.append(board[j][i])
        if run_counter(evaluation_list, token):
            return True
        evaluation_list = []
    
    return False

# Checks if the game is a draw
def check_if_draw(board):
    for row in board:
        if "-" in row:
            return False
    return True

if __name__ == "__main__":
    board = []
    isGameOver = False
    isPlayerOneTurn = True

    board_height = int(input("What would you like the height of the board to be? "))
    board_length = int(input("What would you like the length of the board to be? "))

    board = initialize_board(board_height, board_length)
    print_board(board)
    print()
    print("Player 1: x\nPlayer 2: o\n")

    while not isGameOver:
        identifier = "Player 1" if isPlayerOneTurn else "Player 2"
        token = "x" if isPlayerOneTurn else "o"
        # Asks the current player to choose a column to insert a chip
        column = int(input(f'{identifier}: Which column would you like to choose? '))
        insert_chip(board, column, token)
        print_board(board)
        print()
        # Checks if the current player has won
        isWin = check_if_winner(board, board_length, board_height, token)
        if isWin:
            if isPlayerOneTurn:
                print("Player 1 won the game!")
            else:
                print("Player 2 won the game!")
            isGameOver = True

        # Checks if the game is a draw
        isDraw = check_if_draw(board)
        if isDraw:
            print("Draw. Nobody wins.")
            isGameOver = True

        # Switches to the other player's turn
        isPlayerOneTurn = not isPlayerOneTurn