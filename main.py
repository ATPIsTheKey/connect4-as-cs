from colorama import Fore, init, Back
init(autoreset=True)

Game_board = []


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


init_game_board()
draw_game_board()
