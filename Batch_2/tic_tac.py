import os
board = [" " for _ in range(9)]

def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} \n---+---+---\n {board[3]} | {board[4]} | {board[5]} \n---+---+---\n {board[6]} | {board[7]} | {board[8]} ")

def get_user_input(board, who):
    # get position from user
    position = int(input(f"Enter the position for {who}: ")) - 1
    if board[position] == " ":
        board[position] = who
    else:
        print("Invalid Position")
        get_user_input(board, who)

def check_winner(board, who):
    # check winner of value in who variable
    # horizontal = [0, 1, 2], [3, 4, 5], [6, 7, 8]
    if  (board[0] == who and board[1] == who and board[2] == who) or \
        (board[3] == who and board[4] == who and board[5] == who) or \
        (board[6] == who and board[7] == who and board[8] == who):
        return True

    # vertical = [0, 3, 6], [1, 4, 7], [2, 5, 8]
    elif(board[0] == who and board[3] == who and board[6] == who) or \
        (board[1] == who and board[4] == who and board[7] == who) or \
        (board[2] == who and board[5] == who and board[8] == who):
        return True

    # diagonal = [0, 4, 8], [2, 4, 6]
    elif(board[0] == who and board[4] == who and board[8] == who) or \
        (board[2] == who and board[4] == who and board[6] == who):
        return True
    
    else:
        return False

def check_draw(board):
    # check whether the game is draw
    if " " in board:
        return False
    else:
        return True

    
while True:
    os.system("cls")
    print_board(board)
    get_user_input(board, "X")
    if check_winner(board, "X"):
        print("X Won the game")
        break
    
    if check_draw(board):
        print("Game Draw")


    os.system("cls")
    print_board(board)
    get_user_input(board, "O")
    if check_winner(board, "O"):
        print("O Won the game")
        break

    if check_draw(board):
        print("Game Draw")