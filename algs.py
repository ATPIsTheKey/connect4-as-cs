Test_game_board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]  # todo: remove later


def check_win_columns(game_board):
    critical_row_index = 3  # row index after which no more chain of 4 discs
                            # can be made

    for column_i in range(len(game_board[0])):
        consecutive = 1
        player_id = game_board[0][column_i]

        for row_i in range(len(game_board)):
            disc_id = game_board[row_i][column_i]

            if disc_id == player_id and disc_id != 0:
                consecutive += 1

                if consecutive == 4:
                    return True

            else:
                if row_i == critical_row_index:  # at this point there can be
                    break                        # no more chain of 4 discs

                consecutive = 1
                player_id = disc_id

    return False


def check_win_diagonals(game_board):
    return


def check_win(game_board):
    game_win = False
    return game_win


print(check_win_columns(Test_game_board))
