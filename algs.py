Test_game_board = [
    [1, 2, 3, 4, 0, 0, 0],
    [3, 1, 1, 2, 2, 2, 2],
    [4, 3, 1, 2, 3, 4, 0],
    [0, 4, 3, 1, 2, 3, 4],
    [0, 0, 4, 3, 1, 2, 3],
    [0, 0, 0, 4, 3, 1, 2]
]  # todo: remove in the future


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
    critical_col_index = 3  # column index after which no more chain of 4
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


def check_win_diagonals_lr(game_board):  # todo: implement critical indices
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


def check_win_diagonals_rl(game_board):  # todo: implement critical indices
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


# todo: unit test win checks
def check_win(game_board):
    if check_win_columns(game_board) or check_win_diagonals_rl(game_board) \
            or check_win_diagonals_lr(game_board) or check_win_rows(game_board):
        return True
    else:
        return False
