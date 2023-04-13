should_continue = True

board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

illustrative_board = [['00', '01', '02'],
                      ['10', '11', '12'],
                      ['20', '21', '22']]


def draw_board(b):
    for i in range(len(b)):
        for j in range(len(b)):
            print(f"{b[i][j]}", end='  ')
        print("\n")
    return b


def make_move(b, row, col, player_symbol):
    b[row][col] = player_symbol


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


def change_player(player_symbol):
    if player_symbol.lower() == 'x':
        print("Player X's turn")
        return 'o'
    elif player_symbol.lower() == 'o':
        print("Player O's turn")
        return 'x'


def is_cell_empty(b, row, col):
    if b[row][col] == ' ':
        return True
    else:
        return False


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


def is_board_full(b):
    for row in b:
        for cell in row:
            if cell == ' ':
                return False
    return True


def read_file(f):
    with open(f, 'r') as file:
        print(f"\n{file.read()}")


read_file("rules.txt")
while should_continue:
    should_continue = game_end(board)
