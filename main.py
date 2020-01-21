import colorama
import os
import colorama as clr


# initialize an empty gameboard
Game_board = [[0 for n in range(7)] for arr in range(6)]
colorama.init(autoreset=True)


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


def input_player_move():
    while True:
        input_value = input("Choose column 1-7: ")

        if input_value.isnumeric():
            if int(input_value) in range(1, 8):
                return int(input_value)

        print("Please input a integer between 1 and 7!")


def check_win_columns(game_board):
    critical_row_index = 3  # row index after which no more chain of 4 discs
                            # can be made

    for col_i in range(len(game_board[0])):
        consec = 1
        player_id = game_board[0][col_i]

        for row_i in range(len(game_board)):
            disc_id = game_board[row_i][col_i]

            if disc_id == player_id and disc_id != 0:
                consec += 1

                if consec == 4:
                    return True
            else:
                if row_i == critical_row_index:
                    break

                consec = 1
                player_id = disc_id

    return False


def check_win_rows(game_board):
    critical_col_index = 4  # column index after which no more chain of 4
                            # discs can be made

    for row_i in range(len(game_board)):
        consec = 1
        player_id = game_board[row_i][0]

        for col_i in range(len(game_board[0])):
            disc_id = game_board[row_i][col_i]

            if disc_id == player_id and disc_id != 0:
                consec += 1

                if consec == 4:
                    return True
            else:
                if row_i == critical_col_index:
                    break

                consec = 1
                player_id = disc_id

    return False


def check_win_diagonals_lr(game_board):
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


def check_win_diagonals_rl(game_board):
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


def check_win(game_board):
    if check_win_columns(game_board) or check_win_diagonals_rl(game_board) \
            or check_win_diagonals_lr(game_board):
        return True
    else:
        return False


def update_board_from_player_move(input_value):
    global Game_board

    row_count = 0
    for row in range(6):
        if Game_board[row][input_value - 1] == 0:
            row_count += 1
    if row_count == 0:
        # Invalid - ask again for input since column full
        print("Column full, please input another move.")
        update_board_from_player_move(input_player_move())
    else:
        Game_board[row_count - 1][input_value - 1] = 1


if __name__ == '__main__':
    screen_clear()
    draw_game_board(Game_board)
    while True:
        valid_move = input_player_move()
        update_board_from_player_move(valid_move)
        screen_clear()
        draw_game_board(Game_board)
        if check_win(Game_board):
            break
