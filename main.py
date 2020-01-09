from colorama import Fore, init, Back

init(autoreset=True)


# Game board array initialization
def init_game_board():
    new_game_board = [[0 for n in range(7)] for arr in range(6)]
    return new_game_board


Game_board = init_game_board()


# Game board drawing function
def draw_game_board():
    board_markers = [1, 2, 3, 4, 5, 6, 7]

    players = {
        'O': u"\u25EF",
        '1': Fore.RED + u"\u25CF",
        '2': Fore.YELLOW + u"\u25CF"
    }

    print(Back.BLUE+' ', end='')
    for v in range(6):
        print(Back.BLUE + Fore.BLACK + str(board_markers[v]), end=Back.BLUE+'  ')
    print(Back.BLUE + Fore.BLACK + str(board_markers[6]), end='')
    print(Back.BLUE + ' ')

    for i in range(6):
        print(Back.CYAN + ' ', end='')
        for j in range(6):
            print(Back.CYAN + Fore.BLACK + players[str(Game_board[i][j])], end=Back.CYAN + '  ')
        print(Back.CYAN + Fore.BLACK + players[str(Game_board[i][6])], end='')
        print(Back.CYAN + ' ')


# Checking if all spaces are filled with player's stuff, hopefully
def check_gameboard_full():
    count = 0
    board_full = False

    for i in range(6):
        for j in range(7):
            if Game_board[i][j] != 0:
                count += 1
    if count == 42:
        board_full = True

    return board_full


# Testing the positioning and conversion
for k in range(4):
    Game_board[5][k] = 1
for p in range(2, 6):
    Game_board[p][6] = 2


if __name__ == '__main__':
    draw_game_board()
    check_gameboard_full()
