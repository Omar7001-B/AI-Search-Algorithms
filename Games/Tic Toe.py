board = 9 * [' ']
def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))

def check_winner(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]
    return None

def available_moves(board):
    return [i for i, val in enumerate(board) if val == ' ']

def minimax(board, depth, maximizing_player):
    winner = check_winner(board)
    if winner:
        return -10 + depth if winner == 'X' else 10 - depth, None
    if ' ' not in board:
        return 0, None
    eval_func = max if maximizing_player else min
    return eval_func((minimax(board[:move] + ['O' if maximizing_player else 'X'] + board[move+1:], depth + 1, not maximizing_player)[0], move) for move in available_moves(board))
def get_move(player):
    while True:
        move = int(input(f"Player {player}, enter your move (1-9): "))
        if move == 0:
            return minimax(board, 0, True)[1]
        if 1 <= move <= 9 and board[move - 1] == ' ':
            return move - 1
        print("Invalid move! Please enter a number between 1 and 9.")

def tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    print_board([str(i+1) for i in range(9)])
    player = 'X'

    while True:
        move = get_move(player)
        board[move] = player
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            break
        if ' ' not in board:
            print("It's a tie!")
            break
        player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
