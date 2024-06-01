import math

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def display_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def evaluate(board):
    if check_winner(board, 'X'):
        return 1
    elif check_winner(board, 'O'):
        return -1
    else:
        return 0

def minimax(board, depth, alpha, beta, is_maximizing):
    score = evaluate(board)
    if score == 1 or score == -1 or is_full(board):
        return score

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board):
    best_val = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, -math.inf, math.inf, False)
                board[i][j] = ' '
                if move_val > best_val:
                    move = (i, j)
                    best_val = move_val
    return move

def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def play_game():
    board = initialize_board()
    current_player = 'O'  # Start with 'O'

    while True:
        display_board(board)
        if current_player == 'O':
            row, col = map(int, input("Enter row and column numbers to place 'O' (e.g., 0 1): ").split())
            if not is_valid_move(board, row, col):
                print("Invalid move. Try again.")
                continue
            board[row][col] = 'O'
            if check_winner(board, 'O'):
                display_board(board)
                print("Player 'O' wins!")
                break
        else:
            row, col = find_best_move(board)
            board[row][col] = 'X'
            if check_winner(board, 'X'):
                display_board(board)
                print("Player 'X' wins!")
                break

        if is_full(board):
            display_board(board)
            print("The game is a draw!")
            break

        current_player = 'X' if current_player == 'O' else 'O'

play_game()
