from Board import Board


class Game:
    board_of_game = Board()

    def __init__(self):
        self.current_turn = 1

    def switch_turn(self):
        if self.current_turn == 1:
            self.current_turn = 2
        else:
            self.current_turn = 1


    def initialize_game_board(self):
        self.board_of_game.create_game_board()
        self.board_of_game.show_game_board()

    def player_turn(self, turn):
        #print("enter col")
        #col = int(input())  # The Server need to send
        col = int(turn)
        row = 5
        while self.board_of_game.list_of_characters[row][col] != "@":
            row -= 1
            if row == -1:
                print("cant put here")
                col = -1
                return row, col
        if self.current_turn == 1:
            self.board_of_game.list_of_characters[row][col] = "R"
        else:
            self.board_of_game.list_of_characters[row][col] = "B"
        self.board_of_game.show_game_board()
        self.switch_turn()
        return row, col

    def check_if_someone_win_in_rows(self):
        list_to_check_row_to_win = []
        for i in range(self.board_of_game.rows):
            list_to_check_row_to_win.append([])
            list_to_check_row_to_win[i] = [self.board_of_game.list_of_characters[i][j] for j in range(self.board_of_game.cols)]
        #print(list_to_check_row_to_win)
        return self.check_if_lists_has_win(list_to_check_row_to_win)

    def check_if_someone_win_in_cols(self):
        list_to_check_col_to_win = []
        for i in range(self.board_of_game.rows + 1):
            list_to_check_col_to_win.append([])
            list_to_check_col_to_win[i] = [self.board_of_game.list_of_characters[j][i] for j in range(self.board_of_game.cols - 1)]

        #print(list_to_check_col_to_win)
        return self.check_if_lists_has_win(list_to_check_col_to_win)


    def check_if_someone_win_in_diagonal_right_to_left(self):
        list_of_diagonal = []
        start = 0
        num_of_col = 0
        check_if_need_to_stay_on_last_row = 0
        for i in range(self.board_of_game.cols + self.board_of_game.rows - 1):
            list_of_diagonal.append([])
            if i <= self.board_of_game.rows - 1:
                start = i
            elif i > self.board_of_game.rows - 1 and check_if_need_to_stay_on_last_row == 0:
                start = self.board_of_game.rows - 1
                check_if_need_to_stay_on_last_row = 1
            # else:
            if check_if_need_to_stay_on_last_row == 0:
                for j in range(start + 1):
                    list_of_diagonal[i].append(self.board_of_game.list_of_characters[start - j][self.board_of_game.cols - 1 - j])
                    # print(self.board_of_game.list_of_characters[start - j][j], end=" ")
                # print()
            else:
                number_of_row = self.board_of_game.rows - 1
                num_of_col += 1
                place_to_start = start
                for j in range(place_to_start + 1):
                    list_of_diagonal[i].append(self.board_of_game.list_of_characters[number_of_row][self.board_of_game.cols - 1 - (num_of_col + j)])
                    # print(self.board_of_game.list_of_characters[number_of_row][num_of_col + j], end=" ")
                    place_to_start = place_to_start - 1
                    number_of_row -= 1
                # print()
                start = start - 1
        #print(list_of_diagonal)
        return self.check_if_lists_has_win(list_of_diagonal)

    def check_if_someone_win_in_diagonal_left_to_right(self):
        list_of_diagonal = []
        start = 0
        num_of_col = 0
        check_if_need_to_stay_on_last_row = 0
        for i in range(self.board_of_game.cols + self.board_of_game.rows - 1):
            list_of_diagonal.append([])
            if i <= self.board_of_game.rows - 1:
                start = i
            elif i > self.board_of_game.rows - 1 and check_if_need_to_stay_on_last_row == 0:
                start = self.board_of_game.rows - 1
                check_if_need_to_stay_on_last_row = 1
            if check_if_need_to_stay_on_last_row == 0:
                for j in range(start + 1):
                    list_of_diagonal[i].append(self.board_of_game.list_of_characters[start - j][j])
            else:
                number_of_row = self.board_of_game.rows - 1
                num_of_col += 1
                place_to_start = start
                for j in range(place_to_start + 1):
                    list_of_diagonal[i].append(self.board_of_game.list_of_characters[number_of_row][num_of_col + j])
                    place_to_start = place_to_start - 1
                    number_of_row -= 1
                start = start - 1
        #print(list_of_diagonal)
        return self.check_if_lists_has_win(list_of_diagonal)


    def check_if_someone_win_in_diagonals(self):
        return self.check_if_someone_win_in_diagonal_right_to_left() or self.\
            check_if_someone_win_in_diagonal_left_to_right()

    def check_if_lists_has_win(self, list_to_check):
        for list_in_lists in list_to_check:
            count = 0
            tav_to_check = list_in_lists[0]
            for i in range(len(list_in_lists)):
                if list_in_lists[i] == tav_to_check and list_in_lists[i] != '@':
                    count += 1
                else:
                    count = 0
                    if i+1 == len(list_in_lists)-1: # before was if i+1 == len(list_in_lists)
                        tav_to_check = list_in_lists[i+1]
                    else:
                        tav_to_check = list_in_lists[i]

                    if list_in_lists[i] == tav_to_check and list_in_lists[i] != '@':
                        count += 1
                if count == 4:
                    #print("win in diagonal")
                    return True
        return False

    def check_if_tie(self):
        for inner_list in self.board_of_game.list_of_characters:
            if "@" in inner_list or self.check_if_win():
                return False
        #print("It's a Tie!")
        return True

    def check_if_win(self):
        return self.check_if_someone_win_in_cols() or self.check_if_someone_win_in_rows() or self.\
            check_if_someone_win_in_diagonals()

    def get_winner(self):
        return 3 - self.current_turn

    def activate_game(self):
        self.initialize_game_board()
        while not self.check_if_win():
            self.player_turn()


