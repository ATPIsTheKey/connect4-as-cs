Game_board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]


def check_win_columns(game_board):
    critical = 3

    for column_i in range(len(game_board[0])):
        consecutive = 0
        player_id = game_board[0][column_i]  # take first columns player id

        for row_i in range(len(game_board)):
            disc_id = game_board[row_i][column_i]
            if disc_id == player_id and disc_id != 0:
                consecutive += 1
            else:
                consecutive = 0
                player_id = game_board[row_i][column_i]
                continue

            if consecutive == 4:
                return True

    print(player_id)
    print(consecutive)

    return False


def check_win(game_board):
    game_win = False

    return game_win


if __name__ == '__main__':
    print()
