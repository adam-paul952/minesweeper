from pyfiglet import figlet_format


def print_greeting():
    """
    Prints the welcome message for the game.

    It displays the available game modes, their board sizes, and the number of mines in each mode.
    """
    print(figlet_format("    Minesweeper", font="speed"))
    print(f"{' ':<4}Game Options: \n")
    print(f"{' ':<4}{'Difficulty':<13} {'Size':<9} {'Mines':<15}")
    print(f"{' ':<4}{'-' * 30}")
    print(f"{' ':<4}{'Beginner':<13} {'9x9':<10} {'10':<15}")
    print(f"{' ':<4}{'Intermediate':<13} {'16x16':<10} {'40':<15}")
    print(f"{' ':<4}{'Expert':<13} {'16x30':<10} {'99':<15}\n")


def print_instructions():
    """
    Prints the instructions for the Minesweeper game.

    The instructions include how to reveal a cell, how to flag a cell, how to remove a flag from a cell,
    how to exit the game, and how to display the instructions again.

    """
    instructions = """
    To play the game, enter the row and column of the cell you want to reveal.
    For example, to reveal the cell in the first row and second column, enter '1 2'.\n
    You can also flag a cell by adding 'f' after the row and column numbers.
    For example, to flag the cell in the first row and second column, enter '1 2 f'.
    To remove a flag, enter the row and column of the flagged cell and choose 'y' to remove the flag.

    To exit the game at any time, press 'Ctrl + C'.\n
    To show these instructions again enter help.

    Let's play Minesweeper!
    """
    print(f"{' ':<4}Instructions:\n")
    print(instructions)


def play_again():
    """
    Asks the user if they want to play again.

    Returns:
        bool: True if the user wants to play again, False otherwise.
    """
    play_again = input("Would you like to play again? [Y]es or [N]o: ")
    return play_again.lower() == "y"
