def draw_board(b):
    for i in range(len(b)):
        for j in range(len(b)):
            print(f"{b[i][j]}", end='  ')
        print("\n")
    return b


def make_move(b, row, col, player_symbol):
    b[row][col] = player_symbol


def change_player(player_symbol):
    if player_symbol.lower() == 'x':
        return 'o'
    elif player_symbol.lower() == 'o':
        return 'x'


def is_cell_empty(b, row, col):
    if b[row][col] == ' ':
        return True
    else:
        return False


def is_board_full(b):
    for row in b:
        for cell in row:
            if cell == ' ':
                return False
    return True


def is_winner(b, player_symbol):
    for row in range(3):
        if b[row][0] == player_symbol and b[row][1] == player_symbol and b[row][2] == player_symbol:
            return True
    for col in range(3):
        if b[0][col] == player_symbol and b[1][col] == player_symbol and b[2][col] == player_symbol:
            return True

    if b[0][0] == player_symbol and b[1][1] == player_symbol and b[2][2] == player_symbol:
        return True

    if b[0][2] == player_symbol and b[1][1] == player_symbol and b[2][0] == player_symbol:
        return True

    return False


def game_end(b):
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != ' ':
            return True
        if b[0][i] == b[1][i] == b[2][i] != ' ':
            return True
    if b[0][0] == b[1][1] == b[2][2] != ' ':
        return True
    if b[0][2] == b[1][1] == b[2][0] != ' ':
        return True

    for row in b:
        for cell in row:
            if cell == ' ':
                return False

    return False


def read_file(f):
    with open(f, 'r') as file:
        print(f"\n{file.read()}")


board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

illustrative_board = [['| 0 0  |', '0 1  |', '0 2 |'],
                      ['| 1 0  |', '1 1  |', '1 2 |'],
                      ['| 2 0  |', '2 1  |', '2 2 |']]

read_file("rules.txt")
draw_board(illustrative_board)
player = "x"

while not game_end(board):
    print(f"It's {player}'s turn")
    try:
        x = int(input("Enter row number (0-2): "))
        y = int(input("Enter column number (0-2): "))

        if x not in [0, 1, 2] or y not in [0, 1, 2]:
            raise ValueError("Please enter a valid number between 0 and 2.")
        elif is_cell_empty(board, x, y):
            make_move(board, x, y, player)
            draw_board(board)

            if is_winner(board, player):
                print(f"Player {player} wins!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break
            else:
                player = change_player(player)
        else:
            print("This cell is already taken, please choose another one.")
    except ValueError as e:
        print(f"{e}\n")

