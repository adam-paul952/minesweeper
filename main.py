from pyfiglet import figlet_format
from board import Board

"""
This dictionary maps the difficulty levels of the game to their corresponding board sizes and number of mines.

Each key is a string representing the difficulty level: "Beginner", "Intermediate", or "Expert".

Each value is a tuple with three elements:
- The first element is the number of rows in the game board.
- The second element is the number of columns in the game board.
- The third element is the number of mines on the game board.

Board sizes and mine counts are as follows:
- Beginner: 9x9 board with 10 mines
- Intermediate: 16x16 board with 40 mines
- Expert: 16x30 board with 99 mines
"""
game_options = {
    "Beginner": (9, 9, 10),
    "Intermediate": (16, 16, 40),
    "Expert": (16, 30, 99),
}


def greeting():
    """
    Prints a greeting message for the Minesweeper game.

    The message includes the game title and instructions on how to get started. It also displays the available game modes, their board sizes, and the number of mines in each mode.

    The game modes are:
    - Beginner: 9x9 board with 10 mines
    - Intermediate: 16x16 board with 40 mines
    - Expert: 16x30 board with 99 mines
    """
    print(figlet_format("minesweeper".upper(), font="standard"))
    print("\nGetting Started:\n")
    print("Select a game mode to play: \n")
    print("{:<13} {:<9} {:<15}".format("Difficulty", "Size", "Mines"))
    print("-" * 30)
    print("{:<13} {:<10} {:<15}".format("Beginner", "9x9", "10"))
    print("{:<13} {:<10} {:<15}".format("Intermediate", "16x16", "40"))
    print("{:<13} {:<10} {:<15}".format("Expert", "16x30", "99\n"))


def get_user_input():
    while True:
        try:
            current_input = input(
                "Enter the row and column to reveal (and optional flag): "
            )
        except KeyboardInterrupt:
            print("\nGame interrupted by user. Exiting...")
            return None, None, False

        parts = current_input.split()

        # Check if the input has 2 or 3 parts
        if len(parts) < 2 or len(parts) > 3:
            print("Invalid input. Please enter 'row col flag (optional)'.")
            continue

        # Check if the first two parts are integers
        try:
            row, col = map(int, parts[:2])
        except ValueError:
            print("Invalid input. 'row' and 'col' should be integers.")
            continue

        # Check if the third part (if it exists) is 'flag'
        flag = False
        if len(parts) == 3:
            if parts[2].lower() == "f":
                flag = True
            else:
                print("Invalid input. The third part should be 'f' for 'flag'.")
                continue

        # If we've reached this point, the input is valid
        return row, col, flag


def game_board(width, height, mines):
    board = Board(width, height, mines)
    board.draw_game_board()
    can_continue = True

    while can_continue:
        row, col, flag = get_user_input()
        if row is None:
            can_continue = False
            break

        if flag:  # Flag cell
            board.player_board[row - 1][col - 1] = "F"
            print("Cell flagged.")
            board.draw_game_board()
        else:  # Reveal cell
            if board.is_mine(row - 1, col - 1):
                print("You hit a mine!\nGame Over.")
                can_continue = False
                board.draw_game_board(True)
            else:
                board.dfs(row - 1, col - 1)
                board.player_board[row - 1][col - 1] = board.default_board[row - 1][
                    col - 1
                ]
                print("Safe move.")
                board.draw_game_board()


def main():
    greeting()
    # Get input from the user to select the game mode
    game_selection = input(
        "\nSelect a game mode: 'B' for Beginner, 'I' for Intermediate, 'E' for Expert: \n"
    ).lower()
    if game_selection == "b":
        print("Beginner mode selected\n")
        game_selection = "Beginner"
    elif game_selection == "i":
        print("Intermediate mode selected\n")
        game_selection = "Intermediate"
    elif game_selection == "e":
        print("Expert mode selected\n")
        game_selection = "Expert"
    else:
        input("Invalid selection. Press any key to exit.\n")
        return

    print(game_options[game_selection], end="\n")
    game_board(*game_options[game_selection])


main()
