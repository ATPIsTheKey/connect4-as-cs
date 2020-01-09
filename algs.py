Game_board = [
    [1, 0, 0, 1, 0, 0, 0],
    [0, 0, 2, 1, 0, 0, 0],
    [1, 0, 1, 2, 0, 0, 0],
    [0, 0, 2, 1, 0, 0, 1],
    [1, 0, 2, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1]
]  # todo: remove later


def check_win_columns(game_board):
    critical = 3

    for column_i in range(len(game_board[0])):
        consecutive = 0
        player_id = game_board[0][column_i]

        for row_i in range(len(game_board)):
            disc_id = game_board[row_i][column_i]

            if disc_id == player_id and disc_id != 0:
                consecutive += 1

                if consecutive == 4:
                    return True

            else:
                if row_i == critical:
                    break

                consecutive = 0
                player_id = disc_id
                continue

    return False


def check_win_diagonals():
    critical = 1  # critical value of initial diagonal 1 is 1
    return


def check_win(game_board):
    game_win = False

    return game_win
