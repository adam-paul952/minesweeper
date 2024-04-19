import os
import time
from messages import print_instructions


def get_user_input():
    """
    Prompts the user for input and processes it.

    The function continuously prompts the user for input until valid input is received.
    Valid input is in the form of 'row col flag (optional)' where 'row' and 'col' are integers,
    and 'flag' is an optional third part that should be 'f' or 'flag' if present.

    The function also handles special commands:
    - 'help' or 'h': Prints the game instructions.
    - 'quit' or 'q': Prompts the user for quit confirmation and quits the game if confirmed.

    In case of a KeyboardInterrupt, the function handles it gracefully by exiting the game.

    Returns:
        tuple: A tuple containing the row and column as integers, and a boolean indicating whether a flag was set.
        If the user chooses to quit the game, the function returns (None, None, False).
    """
    while True:
        try:
            current_input = input(
                "\nEnter the row and column to reveal (and optional flag): "
            )
            print()
            if current_input.lower() in ["help", "h"]:
                print_instructions()
                continue
            elif current_input.lower() in ["quit", "q"]:
                quit_confirmation = input(
                    "Are you sure you want to quit? [y]es or [n]o: "
                )
                if quit_confirmation.lower() in ["y", "yes"]:
                    print("Thanks for playing!")
                    time.sleep(2)
                    os.system("cls")
                    return None, None, False

        except KeyboardInterrupt:
            print("\nGame interrupted by user. Exiting the game...")
            time.sleep(2)
            os.system("cls")
            exit()

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
            if parts[2].lower() in ["f", "flag"]:
                flag = True
            else:
                print("Invalid input. The third part should be 'f' for 'flag'.")
                continue

        # If we've reached this point, the input is valid
        return row, col, flag


game_modes = {"b": "Beginner", "i": "Intermediate", "e": "Expert", "q": "Quit"}


def start_game():
    """
    This function prompts the user to select a game mode and returns the selected mode.

    Returns:
        str: The selected game mode.
    """
    start_string = """
    Select a game mode: \n
    - [B]eginner\n  
    - [I]ntermediate\n  
    - [E]xpert\n  
    - [Q]uit\n\n
    """
    game_selection = input(start_string).lower()

    if game_selection in game_modes:
        if game_selection == "q":
            print("Quitting game.\n")
            exit()
        else:
            print(f"{game_modes[game_selection]} mode selected\n")
            game_selection = game_modes[game_selection]
    else:
        input("Invalid selection. Press any key to exit.\n")
        return

    return game_selection
