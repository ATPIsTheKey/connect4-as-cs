from colorama import Fore, init, Back

init(autoreset=True)

Game_board = []


# u"\u25CF" is the code for a circle


# Game board array initialization
def init_game_board():
    global Game_board
    for i in range(6):
        Game_board.append([])
        for j in range(7):
            Game_board[i].append("O")


# Game board drawing function
def draw_game_board():
    for i in range(6):
        print(Back.CYAN + ' ', end='')
        for j in range(6):
            print(Back.CYAN + Fore.BLACK + str(Game_board[i][j]), end=Back.CYAN + '  ')
        print(Back.CYAN + Fore.BLACK + str(Game_board[i][6]), end='')
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


init_game_board()
draw_game_board()
check_gameboard_full()
