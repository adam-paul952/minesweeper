from pyfiglet import figlet_format


def print_greeting():
    """
    Prints a greeting message for the Minesweeper game.

    The message includes the game title and instructions on how to get started.
    It also displays the available game modes, their board sizes, and the number of mines in each mode.
    """
    print(figlet_format("minesweeper".upper(), font="standard"))
    print("Instructions:\n")
    print("Game Options: \n")
    print("{:<13} {:<9} {:<15}".format("Difficulty", "Size", "Mines"))
    print("-" * 30)
    print("{:<13} {:<10} {:<15}".format("Beginner", "9x9", "10"))
    print("{:<13} {:<10} {:<15}".format("Intermediate", "16x16", "40"))
    print("{:<13} {:<10} {:<15}".format("Expert", "16x30", "99\n"))


def print_instructions():
    """
    Prints the instructions for the Minesweeper game.

    The instructions include how to reveal a cell, how to flag a cell, how to remove a flag from a cell,
    how to exit the game, and how to display the instructions again.

    """
    instructions = """
    To play the game, enter the row and column of the cell you want to reveal.
    For example, to reveal the cell in the first row and second column, enter '1 2'.
    You can also flag a cell by adding 'f' after the row and column numbers.
    For example, to flag the cell in the first row and second column, enter '1 2 f'.
    To remove a flag, enter the row and column of the flagged cell and choose 'y' to remove the flag.

    To exit the game at any time, press 'Ctrl + C'.
    To show these instructions again enter help.

    Let's play Minesweeper!
    """

    print(instructions)


def play_again():
    """
    Asks the user if they want to play again.

    Returns:
        bool: True if the user wants to play again, False otherwise.
    """
    play_again = input("Would you like to play again? [Y]es or [N]o: ")
    return play_again.lower() == "y"
