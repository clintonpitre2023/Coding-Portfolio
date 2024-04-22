def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],  # across the top
        [board[1][0], board[1][1], board[1][2]],  # across the middle
        [board[2][0], board[2][1], board[2][2]],  # across the bottom
        [board[0][0], board[1][0], board[2][0]],  # down the left side
        [board[0][1], board[1][1], board[2][1]],  # down the middle
        [board[0][2], board[1][2], board[2][2]],  # down the right side
        [board[0][0], board[1][1], board[2][2]],  # diagonal
        [board[2][0], board[1][1], board[0][2]]   # diagonal
    ]
    return [player, player, player] in win_conditions

def get_move(player):
    while True:
        try:
            row = int(input(f"{player}, enter the row (0-2): "))
            col = int(input(f"{player}, enter the column (0-2): "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Row and column must be between 0 and 2.")
        except ValueError:
            print("Please enter valid integers.")

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0
    moves_count = 0

    while True:
        current_player = players[turn % 2]
        print_board(board)
        print(f"It's {current_player}'s turn.")

        row, col = get_move(current_player)
        if board[row][col] == " ":
            board[row][col] = current_player
            moves_count += 1
            if check_win(board, current_player):
                print_board(board)
                print(f"Congratulations {current_player}, you have won!")
                break
            elif moves_count == 9:
                print_board(board)
                print("The game is a draw!")
                break
            turn += 1
        else:
            print("This cell is already taken. Please choose another.")

if __name__ == "__main__":
    main()
