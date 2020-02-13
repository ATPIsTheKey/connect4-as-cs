import os

import colorama as clr


def draw_game_board(game_board):
    players = {
        '0': u"\u25EF",
        '1': clr.Fore.RED + u"\u25CF",
        '2': clr.Fore.YELLOW + u"\u25CF"
    }

    print(clr.Back.BLUE + ' ', end='')
    for v in range(6):
        print(clr.Back.BLUE + clr.Fore.BLACK + str(v + 1), end=clr.Back.BLUE + '  ')
    print(clr.Back.BLUE + clr.Fore.BLACK + '7', end='')
    print(clr.Back.BLUE + ' ')

    for i in range(6):
        print(clr.Back.CYAN + ' ', end='')
        for j in range(6):
            print(clr.Back.CYAN + clr.Fore.BLACK + players[str(game_board[i][j])],
                  end=clr.Back.CYAN + '  ')
        print(clr.Back.CYAN + clr.Fore.BLACK + players[str(game_board[i][6])], end='')
        print(clr.Back.CYAN + ' ')


def screen_clear():
    os.system('clear' if os.name == 'posix' else 'cls')


def check_gameboard_full(game_board):
    count = 0
    board_full = False

    for i in range(6):
        for j in range(7):
            if game_board[i][j] != 0:
                count += 1
    if count == 42:
        board_full = True

    return board_full


def input_player_move(player):
    while True:
        input_value = input("Player {}, please choose a column 1-7: ".format(
            player)
        )

        if input_value.isnumeric():
            if int(input_value) in range(1, 8):
                return int(input_value)

        print("Input must be between 1 and 7!")


def check_gameboard_win_columns(game_board):
    for col_i in range(len(game_board[0])):
        consec = 0
        player_id = game_board[0][col_i]

        for row_i in range(len(game_board)):
            disc_id = game_board[row_i][col_i]

            if disc_id == player_id and disc_id != 0:
                consec += 1

                if consec == 4:
                    return True
            else:
                consec = 1
                player_id = disc_id

    return False


def check_gameboard_win_rows(game_board):
    for row_i in range(len(game_board)):
        consec = 0
        player_id = game_board[row_i][0]

        for col_i in range(len(game_board[0])):
            disc_id = game_board[row_i][col_i]

            if disc_id == player_id and disc_id != 0:
                consec += 1

                if consec == 4:
                    return True
            else:
                consec = 1
                player_id = disc_id

    return False


def check_gameboard_win_diagonals_lr(game_board):
    for off in range(3):
        consec_inner = consec_outer = 0
        player_id_inner = game_board[0][0]
        player_id_outer = game_board[0][1]

        for i in range(6 - off):
            disc_id_inner = game_board[i + off][i]
            disc_id_outer = game_board[i][i + off + 1]

            if disc_id_inner == player_id_inner and disc_id_inner != 0:
                consec_inner += 1

                if consec_inner == 4:
                    return True
            else:
                consec_inner = 1
                player_id_inner = disc_id_inner

            if disc_id_outer == player_id_outer and disc_id_outer != 0:
                consec_outer += 1

                if consec_outer == 4:
                    return True
            else:
                consec_outer = 1
                player_id_outer = disc_id_outer

    return False


def check_gameboard_win_diagonals_rl(game_board):
    for off in range(3):
        consec_inner = consec_outer = 0
        player_id_inner = game_board[0][6]
        player_id_outer = game_board[0][5]

        for i in range(6 - off):
            disc_id_inner = game_board[i + off][6 - i]
            disc_id_outer = game_board[i][6 - (i + off + 1)]

            if disc_id_inner == player_id_inner and disc_id_inner != 0:
                consec_inner += 1

                if consec_inner == 4:
                    return True
            else:
                consec_inner = 1
                player_id_inner = disc_id_inner

            if disc_id_outer == player_id_outer and disc_id_outer != 0:
                consec_outer += 1

                if consec_outer == 4:
                    return True
            else:
                consec_outer = 1
                player_id_outer = disc_id_outer

    return False


def check_gameboard_win(game_board):
    return check_gameboard_win_columns(game_board) or check_gameboard_win_diagonals_rl(game_board) \
           or check_gameboard_win_diagonals_lr(game_board) or check_gameboard_win_rows(game_board)


def update_board_from_player_move(game_board, input_value, player_id):
    row_count = 0

    for row in range(6):
        if game_board[row][input_value - 1] == 0:
            row_count += 1

    if row_count == 0:
        print("Column full, please input another move!")
        game_board = update_board_from_player_move(
            game_board, input_player_move(player_id), player_id)
    else:
        game_board[row_count - 1][input_value - 1] = player_id

    return game_board


if __name__ == '__main__':
    # initialize everything
    Game_board = [[0 for n in range(7)] for arr in range(6)]
    clr.init(autoreset=True)
    current_player = 2  # todo: looks ugly

    screen_clear()
    draw_game_board(Game_board)

    while True:
        try:
            if current_player == 1:
                current_player = 2
            else:
                current_player = 1

            valid_move = input_player_move(current_player)
            Game_board = update_board_from_player_move(
                Game_board, valid_move, current_player)
            screen_clear()
            draw_game_board(Game_board)

            if check_gameboard_full(Game_board):
                print("Board is full. Game has ended.")
                break

            if check_gameboard_win(Game_board):
                print("Player {pl} has won the game!".format(pl=current_player))
                break

        except KeyboardInterrupt:
            break
