board = [" " for _ in range(9)]


def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} \n---+---+---\n {board[3]} | {board[4]} | {board[5]} \n---+---+---\n {board[6]} | {board[7]} | {board[8]} ")


def get_user_input(turn):
    position = int(input(f"Enter the position for {turn}: ")) - 1
    board[position] = turn


# check winner
def check_winner(board, turn):
    # horizontal
    if (board[0] == turn and board[1] == turn and board[2] == turn) or \
       (board[3] == turn and board[4] == turn and board[5] == turn) or \
       (board[6] == turn and board[7] == turn and board[8] == turn):
        return True
    #vertical
    elif (board[0] == turn and board[3] == turn and board[6] == turn) or \
         (board[1] == turn and board[4] == turn and board[7] == turn) or \
         (board[2] == turn and board[5] == turn and board[8] == turn):
        return True
    # diagonal
    elif (board[0] == turn and board[4] == turn and board[8] == turn) or \
         (board[2] == turn and board[4] == turn and board[6] == turn):
         return True
    else:
        return False


def check_draw(board):
    # check the draw condition
    if " " in board:
        return False
    else:
        return True


while True:
    print_board(board)
    get_user_input("X")
    print_board(board)
    get_user_input("O")
    if check_winner(board, "X"):
        print("X is the winner")
        print_board(board)
        break
    elif check_winner(board, "O"):
        print("O is the winner")
        print_board(board)
        break
    elif check_draw(board):
        print("Game is draw")
        print_board(board)
        break