from game import Game
from messages import print_greeting, print_instructions, play_again
from user_input import start_game

"""
Dictionary that stores the game options.

Each key is a string representing the difficulty level: 
- Beginner:     9x9 board with 10 mines
- Intermediate: 16x16 board with 40 mines
- Expert:       16x30 board with 99 mines

Each value is a tuple with three elements:
- The first element is the number of columns in the game board.
- The second element is the number of rows in the game board.
- The third element is the number of mines on the game board.
"""
game_options = {
    "Beginner": (9, 9, 10),
    "Intermediate": (16, 16, 40),
    "Expert": (16, 30, 99),
}


def main():
    """
    This is the main function for the game. It handles the game loop and user interactions.

    The function first prints a greeting and instructions for the game. Then, it enters a loop
    where it continuously starts new games until the user decides to quit.

    In each iteration of the loop, the function does the following:
    1. Starts a new game based on the user's selection.
    2. Creates a new Game instance with the selected game options.
    3. Enters a nested loop where it continuously plays the game until the game is over.
    4. After the game is over, it increments the games_played counter.
    5. Asks the user if they want to play again. If the user decides to quit, it breaks the loop.

    Finally, it prints a farewell message and the program ends.
    """
    games_played = 1

    print_greeting()
    print_instructions()

    game_selection = start_game()

    while True:
        game = Game(game_options[game_selection], games_played)

        while game.playing:
            games_played += 1
            game.play_game()

        if not play_again():
            break

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
