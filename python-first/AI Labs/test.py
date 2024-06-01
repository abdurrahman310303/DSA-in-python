# my_dict = {'c': 3, 'a': 9, 'b': 2}

# # Sorting by keys
# sorted_by_keys = dict(sorted(my_dict.items()))
# print("Sorted by keys:", sorted_by_keys)
# x = 10
# print(isinstance(x, int))  # Output: True
# print(isinstance(x, float))  # Output: False



# # Creating a 3x3 tic-tac-toe board
tic_tac_toe_board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Function to print the board (for visualization purposes)
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Function to check if either player has won
def check_winner(board):
    # Check rows for a win
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return f"Player {row[0]} wins!"

    # Check columns for a win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return f"Player {board[0][col]} wins!"

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return f"Player {board[0][0]} wins!"
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return f"Player {board[0][2]} wins!"

    # No winner
    return None

# Function to check for a draw
def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# Main game loop
def play_game():
    current_player = 'X'
    while True:
        print_board(tic_tac_toe_board)
        print(f"Player {current_player}'s turn")

        # Take input from the user
        row = int(input("Enter the row (0, 1, 2): "))
        col = int(input("Enter the column (0, 1, 2): "))

        # Check if the cell is empty
        if tic_tac_toe_board[row][col] == ' ':
            tic_tac_toe_board[row][col] = current_player
        else:
            print("Cell already taken. Try again.")
            continue

        # Check for a winner
        winner = check_winner(tic_tac_toe_board)
        if winner:
            print_board(tic_tac_toe_board)
            print(winner)
            break

        # Check for a draw
        if check_draw(tic_tac_toe_board):
            print_board(tic_tac_toe_board)
            print("It's a draw!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()


# print("   |", end="")
# for i in range(1, 11):
#     print(f" {i:2}", end="")
# print()  # New line

# # Print separator
# print("---+" + "---"*10)

# # Print multiplication table
# for i in range(1, 11):
#     print(f" {i:2} |", end="")
#     for j in range(1, 11):
#         result = i * j
#         print(f" {result:2}", end="")
#     print()  # Move to the next line

# class BankAccount:
#     def __init__(self, balance=0):
#         self.balance = balance

#     def withdraw(self, amount):
#         if amount > 0 and self.balance >= amount:
#             self.balance -= amount
#             print(f"Withdrew {amount}. New balance: {self.balance}")
#         else:
#             print("Withdrawal failed. Insufficient funds.")

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited {amount}. New balance: {self.balance}")
#         else:
#             print("Deposit failed. Invalid amount.")

# # Example usage
# account = BankAccount(1000)
# print("Initial balance:", account.balance)

# account.withdraw(500)
# account.deposit(200)
# account.withdraw(800)
# account.withdraw(1000)
