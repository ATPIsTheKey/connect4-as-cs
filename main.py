from colorama import Fore, init, Back
init(autoreset=True)

global Game_board
Game_board = []


# Game board array initialization
def init_game_board():
    for i in range(6):
        Game_board.append([])
        for j in range(7):
            Game_board[i].append(u"\u25CF")


# Game board drawing function design 1
# def draw_game_board():
#     for i in range(6):
#         print(Fore.GREEN + " || ", end='')
#         for j in range(6):
#             print(Back.CYAN + str(Game_board[i][j]), end=Fore.GREEN + '|')
#         print(Back.CYAN + str(Game_board[i][6]), end=' ')
#         print(Fore.GREEN + "||")
#         print(Fore.GREEN + " ++---+--+--+--+--+--+---++")
    # for i in range(8):
    #     print(Fore.GREEN + " - -", end='')


def draw_game_board():
    for i in range(6):
        print(Back.CYAN + ' ', end='')
        for j in range(6):
            print(Back.CYAN + Fore.BLACK + str(Game_board[i][j]), end=Back.CYAN + '  ')
        print(Back.CYAN + Fore.BLACK + str(Game_board[i][6]), end='')
        print(Back.CYAN + ' ')


init_game_board()
draw_game_board()
