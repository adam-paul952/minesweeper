from random import sample


class Board:
    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.mines = mines
        self.mine_cells = []
        self.flagged_cells = []
        self.player_board = self.initialize_player_board()
        self.default_board = self.initialize_default_board()

    def initialize_player_board(self):
        return [["*" for _ in range(self.width)] for _ in range(self.height)]

    def initialize_default_board(self):
        default_board = [[" " for _ in range(self.width)] for _ in range(self.height)]

        all_cells = [
            (i, j) for i in range(1, self.height) for j in range(1, self.width)
        ]

        self.mine_cells = sample(all_cells, self.mines)

        for i, j in self.mine_cells:
            default_board[i][j] = "M"
            for x in range(max(0, i - 1), min(i + 2, self.height)):
                for y in range(max(0, j - 1), min(j + 2, self.width)):
                    if default_board[x][y] != "M":
                        if default_board[x][y] == " ":
                            default_board[x][y] = "1"
                        else:
                            default_board[x][y] = str(int(default_board[x][y]) + 1)
        return default_board

    def draw_game_board(self, reveal=False):
        """
        Prints the current state of the game board.

        Args:
        reveal (bool, optional): If True, the function prints the default game board (revealing all cells). If False, the function prints the player's game board (with unrevealed cells). Defaults to False.

        The function first prints a row of column numbers. Then, for each row in the game board, it prints the row number, followed by the cell values in that row.

        Each cell value is printed inside a box, and there's a line of dashes under each row to separate it from the next row.

        Example:
        If the player's game board is [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']], and the default game board is [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']], the function will print:

          | 1 | 2 | 3 |
        -----------------
        1 | * | * | * |
        -----------------
        2 | * | * | * |
        -----------------
        3 | * | * | * |
        -----------------

        If reveal is True, the function will print:

          | 1 | 2 | 3 |
        -----------------
        1 | 1 | 2 | 3 |
        -----------------
        2 | 4 | 5 | 6 |
        -----------------
        3 | 7 | 8 | 9 |
        -----------------
        """
        # Choose the board to draw
        board_to_draw = self.default_board if reveal else self.player_board

        separator = " | "
        row_template = separator.join(
            ["{} " if i >= 9 else "{}" for i in range(self.width)]
        )
        row_length = len(row_template) - 2 - max(0, self.width - 9)

        # Print the top row of numbers
        print(
            f"  {separator.rstrip()}",
            separator.join(str(i) for i in range(1, self.width + 1)),
            separator.strip(),
        )

        # Print the line under the top row of numbers
        print("-" * row_length)

        # Print the rows with numbers on the left side and the actual values from the default game board inside
        for i in range(self.height):
            row = board_to_draw[i]
            formatted_row = row_template.format(*row)
            print(f"{ i + 1 : 2} {separator.strip()}", formatted_row, separator.strip())
            print("-" * row_length)

    def is_mine(self, row: int, col: int) -> bool:
        """
        Checks if the cell at the given row and column contains a mine.

        Args:
        row (int): The row of the cell to check.
        col (int): The column of the cell to check.

        Returns:
        bool: True if the cell contains a mine, False otherwise.
        """
        return self.default_board[row][col] == "M"

    def dfs(self, row: int, col: int):
        """
        Performs a Depth-First Search (DFS) on the game board starting from a given cell.

        Args:
        row (int): The row number of the cell where the DFS should start.
        col (int): The column number of the cell where the DFS should start.

        The function explores the game board by moving from the starting cell to its unexplored neighbors.
        If a cell is empty, all its neighbors are added to the stack to be explored. The function continues
        until all reachable cells have been explored.

        The player's view of the game board is updated as cells are explored: each unexplored cell ("*") is
        replaced with its corresponding value from the actual game board.

        Note: This function modifies the player_board in-place.
        """
        # List of all 8 possible directions
        directions = [
            (0, 1),  # move right
            (0, -1),  # move left
            (1, 0),  # move down
            (-1, 0),  # move up
            (1, 1),  # move down-right
            (1, -1),  # move down-left
            (-1, 1),  # move up-right
            (-1, -1),  # move up-left
        ]

        # Stack for DFS
        stack = [(row, col)]

        while stack:
            r, c = stack.pop()
            if self.player_board[r][c] == "*":
                self.player_board[r][c] = self.default_board[r][c]
                if self.default_board[r][c] == " ":
                    # If the cell is empty, add all its neighbors to the stack
                    for delta_row, delta_col in directions:
                        new_row, new_col = r + delta_row, c + delta_col
                        if (
                            0 <= new_row < self.height
                            and 0 <= new_col < self.width
                            and self.player_board[new_row][new_col] == "*"
                        ):
                            stack.append((new_row, new_col))

    def flag_mine(self, row, col):
        """
        Flags a cell as containing a mine.

        Args:
        row (int): The row number of the cell to flag.
        col (int): The column number of the cell to flag.

        The function updates the player's game board to flag the cell at the given row and column.
        The cell is marked with an "F" to indicate that the player believes it contains a mine.

        Note: This function modifies the player_board in-place.
        """
        self.player_board[row][col] = "F"
        print("\nCell flagged.")
        self.flagged_cells.append((row, col))
        self.draw_game_board()

    def remove_flag(self, row: int, col: int):
        """
        Removes the flag from a cell.

        Args:
        row (int): The row number of the cell to unflag.
        col (int): The column number of the cell to unflag.

        The function updates the player's game board to remove the flag from the cell at the given row and column.
        The cell is marked with a "*" to indicate that the player is unsure if it contains a mine.

        Note: This function modifies the player_board in-place.
        """
        self.player_board[row][col] = "*"
        self.flagged_cells.remove((row, col))
        self.draw_game_board()

    def check_win(self) -> bool:
        """
        Checks if the player has won the game.

        The player wins the game if all the mine cells have been correctly flagged
        or if the only cells on the player's game board that still contain a "*" are
        the mine cells. This is determined by comparing the mine_cells and flagged_cells
        lists and by checking the player's game board. If the conditions are met,
        the function returns True; otherwise, it returns False.

        Returns:
        bool: True if the player has won the game, False otherwise.
        """
        if set(self.mine_cells) == set(self.flagged_cells):
            return True

        for i in range(self.height):
            for j in range(self.width):
                if self.player_board[i][j] == "*" and (i, j) not in self.mine_cells:
                    return False

        return True

    def get_cell_value(self, row: int, col: int, board="player_board") -> str:
        """
        Returns the value at a specific cell in a given board.

        Args:
        board (str): The name of the board ("player_board" or "default_board").
        row (int): The row number of the cell.
        col (int): The column number of the cell.

        Returns:
        str: The value at the specified cell in the specified board.
        """
        if board == "player_board":
            return self.player_board[row][col]
        elif board == "default_board":
            return self.default_board[row][col]
        else:
            raise ValueError(
                "Invalid board name. Must be 'player_board' or 'default_board'."
            )

    def reveal_cell(self, row, col):
        """
        Reveals the cell at the given row and column.

        Args:
        row (int): The row number of the cell to reveal.
        col (int): The column number of the cell to reveal.

        The function updates the player's game board to reveal the cell at the given row and column.
        If the cell contains a mine, the game is over, and the function returns False.
        If the cell is empty, the function performs a Depth-First Search (DFS) to reveal all connected empty cells.
        If the cell is a number, the function reveals the cell and returns True.

        Returns:
        bool: True if the cell is a number, False if the cell is a mine.
        """
        if self.is_mine(row, col):
            print("You hit a mine!\nGame Over.")
            self.draw_game_board(True)
            return False

        elif (
            self.get_cell_value(row, col) != "*"
            and self.get_cell_value(row, col) != "F"
        ):
            print("\nCell already revealed.")
            return True

        self.dfs(row, col)
        self.player_board[row][col] = self.default_board[row][col]
        print("Safe move.")
        self.draw_game_board()
        return True
