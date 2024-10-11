board = [0 for i in range(9)]

def print_board():
    print(str(board[0]), "|", str(board[1]), "|", str(board[2]))
    print("-----")
    print(str(board[3]), "|", str(board[4]), "|", str(board[5]))
    print("-----")
    print(str(board[6]), "|", str(board[7]), "|", str(board[8]))

def check_winner():
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),(0, 3, 6), (1, 4, 7), (2, 5, 8),(0, 4, 8), (2, 4, 6)]
    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] and board[a] == 0:
            return board[a]
    return None

def tic_tac_toe():
    player = "X"
    for _ in range(9):
        print_board()
        print("Гравець",player,", введіть номер клітинки (0-8):")

        move = int(input())

        if board[move] == 0:  # Якщо клітинка порожня (0)
            board[move] = player
        else:
            print("Клітинка зайнята cпробуйте знову")
            continue

        winner = check_winner()
        if winner:
            print_board()
            print("Переможець:",winner)
            return

        player = "O" if player == "X" else "X"

    print_board()
    print("Нічия")

tic_tac_toe()
