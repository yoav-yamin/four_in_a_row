class Board:
    ROWS = 6
    COLS = 7

    def __init__(self):
        self.list_of_characters = []

    @property
    def rows(self):
        return self.ROWS

    @property
    def cols(self):
        return self.COLS

    def create_game_board(self):
        for i in range(self.ROWS):
            self.list_of_characters.append(["@"] * self.COLS)


    def show_game_board(self):
        print('\n'.join([' '.join([str(num).ljust(2) for num in row]) for row in self.list_of_characters]))

