import os
import random

WIN_LINES = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]]
COMP_MK = "O"
HUM_MK = "X"
WIN_COUNT = 3
NEAR_WIN_COUNT = 2
BEST_SQR = 5

def initialize_board():
    board = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board

def print_board(board):

    grid = f"""
    You are {HUM_MK}, Computer is {COMP_MK}.
    Unclaimed squares are numbered.\n
    Choose a square: {join_or(board, "or")}\n
            |     |
         {board[1]}  |  {board[2]}  |  {board[3]}
            |     |
        ----+-----+----
            |     |
         {board[4]}  |  {board[5]}  |  {board[6]}
            |     |
        ----+-----+----
            |     |
         {board[7]}  |  {board[8]}  |  {board[9]}
            |     |
        """
    print(grid)

def prompt(message):
    print(f"==> {message}")

def valid_squares(board):
    return [board[cell] for cell in range(len(board)) 
                        if board[cell] not in [HUM_MK, COMP_MK, None]]

def check_valid(board, sqr):
    try:
        if int(sqr) in valid_squares(board):
            return True
    except ValueError:
        prompt("Please enter an open number square from 1 to 9")
        return False
    prompt("Please enter an open number square from 1 to 9")
    return False

def player_turn(board):
   # os.system('clear')
    print_board(board)

    while True:
        prompt("Choose a square: ")
        square = input()
        if check_valid(board, square):
            break

    board[int(square)] = HUM_MK

    return board

def computer_turn(board):
    computer_sqr = strategize(board)

    if not computer_sqr:
        valid_moves = valid_squares(board)
        sqr_idx = random.randint(0, len(valid_moves) - 1)
        computer_sqr = valid_moves[sqr_idx]
    
    board[computer_sqr] = COMP_MK
    prompt(f"Computer chose square {computer_sqr}")

def winner(board):
    for line in WIN_LINES:
        board_line = [board[line[0]], board[line[1]], board[line[2]]]
        if board_line.count(HUM_MK) == WIN_COUNT:
            prompt("Congratulations! You won the game!")
            print_board(board)
            return True
        elif board_line.count(COMP_MK) == WIN_COUNT:
            prompt("Oops! Computer won the game!")
            print_board(board)
            return True
    return False

def full_board(board):
    if not valid_squares(board):
        return True
    return False

def join_or(board, delimiter):
    if not board:
        return ""

    msg_list = [str(num) for num in board if isinstance(num, int)]
    end_char = msg_list.pop()

    if not msg_list:
        return end_char
    elif len(msg_list) == 1:
        return f"{msg_list[0]} {delimiter} {end_char}"
    else:
        return f"{", ".join(msg_list)} {delimiter} {end_char}"

def strategize(board):
    for line in WIN_LINES:
        board_line = [board[line[0]], board[line[1]], board[line[2]]]
        if board_line.count(COMP_MK) == NEAR_WIN_COUNT and board_line.count(HUM_MK) == 0:
            return valid_squares(board_line).pop()
    
    for line in WIN_LINES:
        board_line = [board[line[0]], board[line[1]], board[line[2]]]
        if board_line.count(HUM_MK) == NEAR_WIN_COUNT and board_line.count(COMP_MK) == 0:
            return valid_squares(board_line).pop()

    if board[BEST_SQR] not in (HUM_MK, COMP_MK):
            return BEST_SQR 

def tic_tac_toe():
    os.system('clear')
    play = "yes"
    prompt("Welcome to Tic-Tac-Toe")

    while play.lower() == "yes":
        board = initialize_board()

        while not winner(board) and not full_board(board):
            player_turn(board)
            join_or(board, "or")
            if not winner(board) and not full_board(board):
                computer_turn(board)

        if full_board(board):
            prompt("All squares are full, the game is a tie.")

        play = ""
        while play.lower() not in ["no", "yes"]:
            prompt("Would you like to play again? Type YES or NO: ")
            play = input()

    prompt("Thank you for playing!")

tic_tac_toe()
