def init_board(board_size):
    board = []
    for row in range(board_size):
        new_row = []
        for column in range(board_size):
            new_row.append(".")
        board.append(new_row)
    return board


def get_move(board, player):
    abc = "ABC"
    """Returns the coordinates of a valid move for player on board."""
    while True:
        inp = input("Enter your cordinate!")
        if not len(inp) == 2:
            print("Not valid")
        else:
            row = abc.find(inp[0])
            col = inp[1] - 1
            if row == -1 and 0 <= col < len(board) - 1:
                print("Cordinate not on the board!")
            else:
                if board[row][col] == '.':
                    return row, col
                else:
                    print("Cordinat already occupied")
        


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    pass


def has_won(board, player):
    """Returns True if player has won the game."""
    return False


def is_full(board):
    """Returns True if board is full."""
    return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    pass


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    row, col = get_move(board, 1)
    mark(board, 1, row, col)

    winner = 0
    print_result(winner)


def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
