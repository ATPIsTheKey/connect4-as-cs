from colorama import Fore, init
init(autoreset=True)

global Game_board
Game_board = []


# Game board array initialization
def init_game_board():
    for i in range(6):
        Game_board.append([])
        for j in range(7):
            Game_board[i].append(0)


# Game board drawing function
def draw_game_board():
    for i in range(6):
        print(Fore.GREEN + " || ", end='')
        for j in range(6):
            print(Game_board[i][j], end=Fore.GREEN + ' | ')
        print(Game_board[i][6], end=' ')
        print(Fore.GREEN + "||")
    for i in range(8):
        print(Fore.GREEN + " - -", end='')


init_game_board()
draw_game_board()