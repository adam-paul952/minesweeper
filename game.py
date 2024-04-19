from board import Board
from user_input import get_user_input

remove_flag_string = "Cell is flagged. [y]es to remove [n]o to cancel: "


class Game:
    def __init__(self, game_selection, games_played):
        """
        Initialize a new game.

        Args:
            game_options (dict): A dictionary containing the options for the game.
                                The keys are the names of the options and the values are the corresponding settings.

        Attributes:
            game_options (dict): Stores the options for the game.
            games_played (int): Stores the number of games played. Initialized to 0.
            playing (bool): A flag indicating whether the game is currently being played. Initialized to True.
        """
        self.game_selection = game_selection
        self.games_played = games_played
        self.playing = True
        self.board = Board(*self.game_selection)

    def print_game_state(self):
        print("\nGame Number:", self.games_played)
        print("\n")
        print("Mines Remaining:", self.board.mines - len(self.board.flagged_cells))
        print("\n")
        self.board.draw_game_board()

    def play_game(self):
        while self.playing:
            self.print_game_state()
            row, col, flag = get_user_input()
            if row is None:
                self.playing = False
                break

            if flag:
                self.board.flag_mine(row - 1, col - 1)
                if self.board.check_win():
                    print("Congratulations! You've won the game.")
                    self.playing = False
                    self.board.draw_game_board(True)

            elif (
                row < 1 or row > self.board.height or col < 1 or col > self.board.width
            ):
                print("Invalid input. Please enter valid row and column numbers.")
                continue

            elif self.board.get_cell_value(row - 1, col - 1) == "F":
                will_remove_flag = input(remove_flag_string).lower()

                if will_remove_flag in ["y", "yes"]:
                    self.board.remove_flag(row - 1, col - 1)

            else:
                self.playing = self.board.reveal_cell(row - 1, col - 1)
