

def print_board(board):
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(board, player):
    # All winning combinations
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in win_combos:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for cell in board)

def play_game():
    board = ['1','2','3','4','5','6','7','8','9']
    current_player = 'X'

    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter a position (1-9): ")

        if move not in '123456789' or board[int(move)-1] in ['X', 'O']:
            print("Invalid move. Try again.")
            continue

        board[int(move)-1] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
if __name__ == "__main__":
    play_game()
